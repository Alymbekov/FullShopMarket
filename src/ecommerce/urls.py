from django.contrib import admin
from django.urls import path, re_path
from .views import (
    index, about_page, contact_page
)

urlpatterns = [
    path('', index),
    re_path(r'^about/$', about_page),
    path('contact/', contact_page),
    path('admin/', admin.site.urls),
]
