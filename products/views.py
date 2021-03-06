from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Product
from .forms import ProductForm


@login_required
def all_products(request):

    products = Product.objects.all().order_by('price')

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


@login_required
def add_product(request):
    """ Edit, delete or add products """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can access this area.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('products'))

        messages.error(request,
                       ('Failed to add product. '
                        'Please ensure the form is valid.'))
    else:
        product_form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'product_form': product_form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('products'))

        messages.error(request,
                       ('Failed to update product. '
                        'Please ensure the form is valid.'))
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
