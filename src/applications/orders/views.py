from django.shortcuts import render
from applications.cart.models import Cart
import random

from .models import Order, Address


def checkout_view(request):
    list_numbers =  [x for x in range(1, 100)]

    if request.method == 'POST':
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        phonenumber = request.POST.get('phonenumber')
        cart_obj, new_obj = Cart.objects.get_or_new(request)
        address, created = Address.objects.get_or_create(
            address1=address1,
            address2=address2,
            phone_number=phonenumber, 
        )

        order_obj, created = Order.objects.get_or_create(
            order_id=random.choice(list_numbers),
            cart=cart_obj,
            status='created',
            shipment_total=10.10,
            address=address
        )
    return render(request, 'checkout/checkout.html', locals())