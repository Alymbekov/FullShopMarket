from django.shortcuts import render
from .models import Cart


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


