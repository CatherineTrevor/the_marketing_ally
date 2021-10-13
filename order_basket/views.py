from django.shortcuts import (
    render, redirect, get_object_or_404, HttpResponse
)
from django.contrib import messages

from products.models import Product


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


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = 1
    minutes = []
    product_minutes = product.time_allocation_mins
    redirect_url = request.POST.get('redirect_url')

    if product_minutes is not None:
        minutes.append(product_minutes)
        total_bag_minutes = sum(minutes)
        if total_bag_minutes >= 180:
            messages.error(request, f'It is only possible to have 3 hours maximum in your basket')
            return redirect(redirect_url)
    bag = request.session.get('bag', {})

    if item_id in bag.keys():
        print('item', item_id)
        bag[item_id] += quantity
        messages.success(request,
                            (f'Updated {product.name} '
                            f'quantity to {bag[item_id]}'))
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
