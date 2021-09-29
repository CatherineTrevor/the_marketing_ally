from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.views.decorators.http import require_POST

from .forms import OrderRequestForm
from .models import OrderRequest


def order_basket(request):

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

    order_request_form = OrderRequestForm()
    template = 'order_basket/order_basket.html'
    context = {
        'order_request_form': order_request_form,
        'stripe_public_key': 'pk_test_51JXPgOAz3izc7KdhHtbrfowpOlxVe3gGMyEh84gBe3nyNpAxDd4VW1Qx017TSCk85GWSEDLqaSXQb96PeytE9hrQ00lbNXI96U',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)


def calendar(request):

    return render(request, 'order_basket/calendar.html')
