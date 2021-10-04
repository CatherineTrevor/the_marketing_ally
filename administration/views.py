from django.shortcuts import render

from contact.models import QuoteRequest


def view_quotes(request):

    return render(request, 'administration/view_quotes.html')
