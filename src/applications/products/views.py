from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        context['key'] = "Value"
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
    instance = get_object_or_404(Product, pk=pk)
    context = {
        'instance': instance
    }
    return render(request, 'products/detail.html', context)








