from django.shortcuts import render, redirect
from .models import Cart
from applications.products.models import Product


def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)
    print('New cart created !')
    return cart_obj


def cart_home(request):
    cart_obj, new_obj = Cart.objects.get_or_new(request)
    context = {
        'carts':  cart_obj,
        'new_obj': new_obj,
        'test': 'test'
    }
    return render(request, 'carts/home.html', context)


def cart_update(request):
    # product_id = request.POST.get('product_id')
    # print(product_id)
    product_id = request.POST.get('product_id')

    product_obj = Product.objects.get(pk=product_id)
    if product_id is not None:
        try:
            product_obj = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            print("Is worl")
            return redirect("cart:home")

        cart_obj, new_obj = Cart.objects.get_or_new(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
        request.session['cart_items'] = cart_obj.products.count()
    return redirect('cart:carts')
