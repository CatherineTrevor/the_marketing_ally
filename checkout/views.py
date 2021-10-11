from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.conf import settings
from django.contrib import messages
from django.views.decorators.http import require_POST

from .forms import OrderRequestForm
from .models import OrderRequest, OrderLineItem

from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from order_basket.contexts import bag_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, ('Sorry, your payment cannot be '
                                 'processed right now. Please try '
                                 'again later.'))
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_request_form = OrderRequestForm(form_data)
        if order_request_form.is_valid():
            form = order_request_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            form.stripe_pid = pid
            form.original_bag = json.dumps(bag)
            form.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't "
                        "found in our database. "
                        "Please call us for assistance!")
                    )
                    form.delete()
                    return redirect(reverse('view_bag'))            

            
            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_confirmation',
                                    args=[form.order_number]))
        else:
            messages.error(request, ('There was an error with your form. '
                                     'Please double check your information.'))
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request,
                        "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = 150
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=100,
            currency=settings.STRIPE_CURRENCY,
        )

        # Attempt to prefill the form with any info
        # the user maintains in their profile
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_request_form = OrderRequestForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_request_form = OrderRequestForm()
        else:
            order_request_form = OrderRequestForm()

    if not stripe_public_key:
        messages.warning(request, ('Stripe public key is missing. '
                                'Did you forget to set it in '
                                'your environment?'))

    template = 'checkout/checkout.html'
    context = {
        'order_request_form': order_request_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_confirmation(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order_request = get_object_or_404(OrderRequest, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order_request.user_profile = profile
        order_request.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order_request.phone_number,
                'default_country': order_request.country,
                'default_postcode': order_request.postcode,
                'default_town_or_city': order_request.town_or_city,
                'default_street_address1': order_request.street_address1,
                'default_street_address2': order_request.street_address2,
                'default_county': order_request.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order_request.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_confirmation.html'
    context = {
        'order_request': order_request,
    }

    return render(request, template, context)
