from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Product

# class ProductSearchView(ListView):
#     queryset = Product.objects.all()
#     template_name = 'products/searchresult.html'


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'
    paginate_by = 1

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        context['featured'] = Product.objects.featured()
        context['page_products'] = True 
        context['search_query'] = self.request.GET.get('search')
        return context

    
    def get_queryset(self):
        queryset = Product.objects.all()
        query_result = self.request.GET.get('search')
        if query_result:
            queryset = Product.objects.filter(
                Q(title__icontains=query_result) |
                Q(description__icontains=query_result)
            )
        return queryset

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




