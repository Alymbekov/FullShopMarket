from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include, re_path
from .views import (
    home_page, about_page, contact_page,
    login_page, register_page,
)

# from products.views import (
#     ProductListView, ProductDetailView,
#     products_list_view, products_detail_view,
#     ProductFeaturedDetailView, ProductFeaturedListView,
#     ProductDetailSlugView,
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name="home"),
    path('about/', about_page, name="about"),
    path('contact/', contact_page, name="contact"),

    path('products/', include(("applications.products.urls", 'applications.products'), namespace='products')),
    # path('products-fbv/', products_list_view, name='productsfbv'),

    # path('products/<int:pk>/', ProductDetailView.as_view()),
    # path('products/<slug:slug>/', ProductDetailSlugView.as_view()),


    # path('products-fbv/<int:pk>/', products_detail_view, name='products-fbv'),

    # path('featured/<int:pk>/', ProductFeaturedDetailView.as_view(),),
    # path('featured/', ProductFeaturedListView.as_view(),),

    path('login/', login_page, name="login_page"),
    path('register/', register_page, name="register_page"),
    path('carts/', include('applications.cart.urls')),
    path('users/', include('applications.users.urls')),
    re_path(r'^about/$', about_page),
    path('orders/', include('applications.orders.urls')),
    path('api/v1/', include('applications.shop_api.urls')),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


