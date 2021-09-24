from django.shortcuts import render
from django.conf import settings

from .forms import OrderForm
from .models import Order


def contact(request):

    if request.method == 'POST':

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'comment': request.POST['comment'],     
        }
        order_form = OrderForm(form_data)

    order_form = OrderForm()    
    template = 'contact/contact.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
