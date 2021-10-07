from django.shortcuts import render, redirect, reverse

from .forms import QuoteRequestForm


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

        if quote_request_form.is_valid():
            form = quote_request_form.save(commit=False)
            form.save()

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('home'))

    quote_request_form = QuoteRequestForm()
    template = 'contact/contact.html'
    context = {
        'quote_request_form': quote_request_form,
    }

    return render(request, template, context)
