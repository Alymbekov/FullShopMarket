from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, re_path, include
from .views import (
    index, about_page, 
    contact_page,
)


app_name = "cart"

urlpatterns = [
    path('', index, name="index"),
    path('carts/', include('applications.cart.urls')),

    path('products/', include('applications.products.urls')),
    path('users/', include('applications.users.urls')),
    re_path(r'^about/$', about_page),
    path('contact/', contact_page),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

