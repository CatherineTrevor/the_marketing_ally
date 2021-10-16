from django.shortcuts import (
    render, redirect, get_object_or_404, HttpResponse, reverse
)
from django.contrib import messages

from products.models import Product
from checkout.forms import OrderRequestForm


def calendar(request):
    """A view that renders the calendar """

    return render(request, 'order_basket/calendar.html')


def order_basket(request):
    """ Render the order basket from which customers can add products """

    products = Product.objects.all().order_by('price')

    context = {
        'products': products,
    }

    return render(request, 'order_basket/order_basket.html', context)


def view_bag(request):
    """ A view to render the bag contents """

    return render(request, 'order_basket/bag.html')


def add_to_bag(request, product_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=product_id)
    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if product_id in bag.keys():
        messages.error(request,
                       (f'{product.name} already exists in your bag'))
    else:
        bag[product_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def add_timeslot_note(request, item_id):
    
    if request.method == "POST":
        form_data = {
            'note': request.POST['note'],
        }
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})
        order_request = OrderRequestForm(form_data)
        bag.update(item_id)
        messages.success(request, f'Succesfully added timeslot')
        context = {
            'order_request': order_request,
        }
        request.session['bag'] = bag
    return (request, context)


def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})
    bag.pop(item_id)
    messages.success(request, f'Removed {product.name} from your bag')
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
