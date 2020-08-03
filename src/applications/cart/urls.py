from django.urls import path

from applications.cart.views import (
    cart_home, cart_update
)

app_name = "cart"

urlpatterns = [
    path('', cart_home, name="carts"),
    path('update/', cart_update, name="update"),
]