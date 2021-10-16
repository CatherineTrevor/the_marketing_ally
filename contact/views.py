from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .forms import QuoteRequestForm
from .models import QuoteRequest


def contact(request):

    if request.method == 'POST':

        form_data = {
            'company_name': request.POST['company_name'],
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'free_consultation_request': request.POST.get(
                'free_consultation_request'),
            'project_name': request.POST['project_name'],
            'project_description': request.POST['project_description'],
        }
        quote_request_form = QuoteRequestForm(form_data)

        if quote_request_form.is_valid():
            form = quote_request_form.save(commit=False)
            form.save()

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('contact_received', args=[form.id]))

    quote_request_form = QuoteRequestForm()
    template = 'contact/contact.html'
    context = {
        'quote_request_form': quote_request_form,
    }

    return render(request, template, context)


def contact_received(request, quote_request_id):

    quote_request = get_object_or_404(QuoteRequest,
                                      quote_request_id=quote_request_id)

    messages.success(request, (f'Request received!'))

    template = 'contact/contact_received.html'
    context = {
        'quote_request': quote_request,
    }

    return render(request, template, context)
