from django.urls import path
from applications.products.views import (
    ProductListView, ProductDetailView,
    products_list_view, products_detail_view,
    ProductFeaturedDetailView, ProductFeaturedListView,
    ProductDetailSlugView,
)

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    # path('products/<int:pk>/', ProductDetailView.as_view()),
    path('<slug:slug>/', ProductDetailSlugView.as_view(), name='detail'),

    path('featured/<int:pk>/', ProductFeaturedDetailView.as_view(),),
    path('featured/', ProductFeaturedListView.as_view(),),
]
