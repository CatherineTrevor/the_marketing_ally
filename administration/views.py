from django.shortcuts import render

from contact.models import QuoteRequest


def view_quotes(request):

    requests = QuoteRequest.objects.all()

    context = {
        'requests': requests,
    }

    return render(request, 'administration/view_quotes.html', context)
