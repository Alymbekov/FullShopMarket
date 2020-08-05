from django.contrib import admin
from .models import Order, Address


class OrderView(admin.ModelAdmin):
    model = Order
    list_display = [
        'id', 'status', 'cart', 
        'total', 'shipment_total'
    ]

class AddressView(admin.ModelAdmin):
    model = Address
    list_display = [
        'id', 'address1', 'address2', 'phone_number'
    ]
admin.site.register(Order, OrderView)
admin.site.register(Address, AddressView)
