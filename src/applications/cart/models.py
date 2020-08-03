from django.db import models
from applications.products.models import Product
from django.contrib.auth import get_user_model

from django.db.models import signals
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

User = get_user_model()


class CartManager(models.Manager):
    def get_or_new(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)


class Cart(models.Model):
    OPENED = 'op'
    CLOSED = 'cl'
    STATUS_CHOICES = (
        (OPENED, 'Opened'),
        (CLOSED, 'Closed'),
    )

    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL
    )

    products = models.ManyToManyField(
        Product, blank=True, related_name='carts',
    )
    objects = CartManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subtotal = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    status = models.CharField(max_length=4, choices=STATUS_CHOICES)

    def __str__(self):
        return str(self.id)


# @receiver(signals.pre_save, sender=Cart)
# def pre_save_cart_receiver(sender, instance, **kwargs):
#     products = instance.products.all()
#     total = 0
#     for x in products:
#         total += x.price
#     print(total)
#     instance.total = total


def m2m_changed_cart_receiver(
    sender, instance,
    action, *args, **kwargs
):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        print("Condition is work")
        total = 0
        for x in instance.products.all():
            total += x.price

        if instance.subtotal != total:
            instance.subtotal = total
            instance.save()


m2m_changed.connect(
    m2m_changed_cart_receiver,
    sender=Cart.products.through)


def pre_save_cart_receiver(sender, instance, *args, **kwargs):
    print(instance.subtotal)
    instance.subtotal = instance.subtotal + 10
    print(instance.subtotal)

signals.pre_save.connect(pre_save_cart_receiver, sender=Cart)
