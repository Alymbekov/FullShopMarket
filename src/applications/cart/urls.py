from django.urls import path

from applications.cart.views import (
    cart_home, cart_update
)

urlpatterns = [
    path('', cart_home, name="carts"),
    path('update/', cart_update),
]