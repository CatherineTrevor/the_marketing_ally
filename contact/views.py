from django.shortcuts import render
from django.conf import settings

from .forms import QuoteRequestForm
from .models import QuoteRequest


def contact(request):

    if request.method == 'POST':

        form_data = {
            'company_name': request.POST['company_name'],
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'free_consultation_request': request.POST['free_consultation_request'],  
            'project_name': request.POST['project_name'],
            'project_description': request.POST['project_description'],                 
        }
        quote_request_form = QuoteRequestForm(form_data)

    quote_request_form = QuoteRequestForm()    
    template = 'contact/contact.html'
    context = {
        'quote_request_form': quote_request_form,
    }

    return render(request, template, context)
