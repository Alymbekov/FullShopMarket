from django.shortcuts import render, redirect
from .models import Cart
from applications.products.models import Product


def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)
    print('New cart created !')
    return cart_obj


def cart_home(request):
    cart_obj_with_status = Cart.objects.get_or_new(request)
    cart_obj = cart_obj_with_status[0]
    products = cart_obj.products.all()
    total = 0
    for x in products:
        total += x.price
    cart_obj.total = total
    cart_obj.save()
    return render(request, 'carts/home.html', locals())


def cart_update(request):
    product_id = 1
    product_obj = Product.objects.get(pk=product_id)
    print(product_obj)
    cart_obj, new_obj = Cart.objects.get_or_new(request)
    if product_obj in cart_obj.products.all():
        print("is work")
        cart_obj.products.remove(product_obj)
    else:
        print('else condition')
        cart_obj.products.add(product_obj)

    return redirect(product_obj.get_absolute_url())
