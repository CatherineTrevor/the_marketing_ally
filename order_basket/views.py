from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib import messages
from django.views.decorators.http import require_POST

from .forms import OrderRequestForm
from .models import OrderRequest

import stripe


def order_basket(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':

        form_data = {
            'account_company_name': request.POST['company_name'],
            'timeslot_option_1': request.POST['timeslot_option_1'],
            'timeslot_option_2': request.POST['timeslot_option_2'],
            'project_name': request.POST['project_name'],
            'project_description': request.POST['project_description'],
        }
        order_request_form = OrderRequestForm(form_data)

        if order_request_form.is_valid():
            form = order_request_form.save(commit=False)
            form.save()

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('home'))

    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=100,
        currency=settings.STRIPE_CURRENCY,
    )

    order_request_form = OrderRequestForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it?')

    template = 'order_basket/order_basket.html'
    context = {
        'order_request_form': order_request_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def calendar(request):

    return render(request, 'order_basket/calendar.html')
