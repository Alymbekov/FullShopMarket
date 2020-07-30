from django.urls import path

from .views import (
    ProductListView, products_list_view,
    ProductDetailView, products_detail_view,
    ProductFeaturedView, ProductBySlugDetailView
)

urlpatterns = [

    path('', ProductListView.as_view(), name="products"),
    path('products-fbv/', products_list_view),

    path('<int:pk>/', ProductDetailView.as_view()),
    path('products-fbv/<int:pk>/', products_detail_view),

    path('featured_products/', ProductFeaturedView.as_view()),
    path('products_by_slug/<slug:slug>/',
         ProductBySlugDetailView.as_view(), name="product"
         ),

]