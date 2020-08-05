from django.urls import path

from ecommerce.views import register_page, login_page

urlpatterns = [
    path('register/', register_page, name="register"),
    path('login/', login_page, name="login"),

]


