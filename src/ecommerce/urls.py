from django.contrib import admin
from django.urls import path, re_path
from .views import (
    index, about_page, 
    contact_page, login_page,
    register_page
)

urlpatterns = [
    path('', index),
    re_path(r'^about/$', about_page),
    path('contact/', contact_page),
    path('register/', register_page),
    path('login/', login_page),
    path('admin/', admin.site.urls),
]
