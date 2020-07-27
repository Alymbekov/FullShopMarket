from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        context['featured'] = Product.objects.featured()
        return context

def products_list_view(request):
    queryset = Product.objects.all()

    context = {
        'object_list': queryset
    }
    return render(request, 'products/list.html', context)


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'
    context_object_name = 'instance'


def products_detail_view(request, pk):
    # instance = get_object_or_404(Product, pk=pk)
   
    obj = Product.objects.get_by_id_s(pk=pk)
    # if obj.exists and obj.count() == 1:
    #     obj = obj.first()
    # else:
    #     raise Http404("Нет такой id для продукта")

    context = {
        'instance': obj
    }
    return render(request, 'products/detail.html', context)



class ProductFeaturedView(ListView):
    template_name = "products/featured.html"
    model = Product

    def get_queryset(self, *args, **kwargs):
        return Product.objects.featured()

class ProductBySlugDetailView(DetailView):
    template_name = "products/detail.html"
    model = Product
    context_object_name = "instance"




