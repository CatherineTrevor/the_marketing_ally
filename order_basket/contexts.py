from django.shortcuts import get_object_or_404

from products.models import Product


def bag_contents(request):

    """ Add items to bag and not allow over 180 minutes
    in any one order """

    bag_items = []
    total = 0
    product_count = 0

    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data

            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })

            print('Middle of process', bag_items)

    grand_total = total

    context = {
        'bag_items': bag_items,
        'grand_total': grand_total,
        'total': total,
        'product_count': product_count,
    }

    print('End of process', bag_items)

    return context
