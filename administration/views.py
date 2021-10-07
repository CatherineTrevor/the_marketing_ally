from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from contact.models import QuoteRequest
from contact.forms import QuoteRequestForm


def view_quotes(request):

    requests = QuoteRequest.objects.all()

    context = {
        'requests': requests,
    }

    return render(request, 'administration/view_quotes.html', context)

@login_required
def edit_quotes(request, quote_id):
    """ Edit a customer quote request """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only administration can enter this area.')
        return redirect(reverse('home'))

    quote = get_object_or_404(QuoteRequest, pk=quote_id)
    if request.method == 'POST':
        form = QuoteRequestForm(request.POST, request.FILES, instance=quote)
        if form.is_valid():
            form.save()
            messages.success(request, 'Quote succesfully update!')
            return redirect(reverse('view_quotes'))
        else:
            messages.error(request,
                           ('Failed to update quote request. '
                            'Please ensure the form is valid.'))
    else:
        form = QuoteRequestForm(instance=quote)
        messages.info(request, f'You are editing {quote.id}')

    template = 'administration/edit_quotes.html'
    context = {
        'form': form,
        'quote': quote,
    }

    return render(request, template, context)
