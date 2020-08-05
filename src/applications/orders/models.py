from django.db import models
from applications.cart.models import Cart

STATUS_CHOICES = (
    ('created','Created'),
    ('paid', 'Paid'),
)




class Address(models.Model):
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50,blank=True) 
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.address1



class Order(models.Model):
    order_id = models.CharField(max_length=100, unique=True, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name = 'orders')
    status = models.CharField(max_length=150, choices=STATUS_CHOICES)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True)
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0, null=True)

    shipment_total = models.DecimalField(max_digits=100, decimal_places=2)


    def __str__(self):
        return str(self.order_id)

