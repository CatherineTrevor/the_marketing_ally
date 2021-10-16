from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from contact.models import QuoteRequest
from contact.forms import QuoteRequestForm
from checkout.models import OrderRequest


@login_required
def view_quotes(request):
    """ View customer orders and quote / contact requests """

    customer_contact = QuoteRequest.objects.all()
    customer_orders = OrderRequest.objects.all()

    template = 'administration/view_quotes.html'

    context = {
        'customer_contact': customer_contact,
        'customer_orders': customer_orders,
    }

    return render(request, template, context)


@login_required
def edit_quotes(request, quote_id):
    """ Edit a customer quote request """
    if not request.user.is_superuser:
        messages.error(request,
                       ('You must be logged in as an '
                        'administrator to access this area.'))
        return redirect(reverse('home'))

    quote = get_object_or_404(QuoteRequest, pk=quote_id)
    if request.method == 'POST':
        form = QuoteRequestForm(request.POST, request.FILES, instance=quote)
        if form.is_valid():
            form.save()
            messages.success(request, 'Quote succesfully updated!')
            return redirect(reverse('view_quotes'))

        messages.error(request,
                       ('Failed to update quote request. '
                        'Please ensure the form is valid.'))
    else:
        form = QuoteRequestForm(instance=quote)
        messages.info(request, f'You are editing {quote.company_name}')

    template = 'administration/edit_quotes.html'
    context = {
        'form': form,
        'quote': quote,
    }

    return render(request, template, context)
