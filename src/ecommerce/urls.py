from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, re_path
from .views import (
    index, about_page, 
    contact_page, login_page,
    register_page
)

from applications.cart.views import cart_home

from applications.products.views import (
    ProductListView, ProductDetailView, 
    products_list_view, products_detail_view,
    ProductFeaturedView, ProductBySlugDetailView

    )

urlpatterns = [
    path('', index, name="index"),
    re_path(r'^about/$', about_page),
    path('contact/', contact_page),
    path('register/', register_page, name="register"),
    path('login/', login_page, name="login"),

    path('products/', ProductListView.as_view(), name="products"),
    path('products-fbv/', products_list_view),

    path('products/<int:pk>/', ProductDetailView.as_view(), name="product"),
    path('products-fbv/<int:pk>/', products_detail_view),

    path('featured_products/', ProductFeaturedView.as_view()),
    path('products_by_slug/<slug:slug>/', ProductBySlugDetailView.as_view()
         ),

    path('carts', cart_home, name="carts"),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

