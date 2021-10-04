from django.shortcuts import render

from products.models import Product


def index(request):

    products = Product.objects.all().order_by('price')

    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)
