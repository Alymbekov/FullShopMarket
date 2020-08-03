from applications.cart.models import Cart
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Product


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.get_or_new(self.request)
        context['carts'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not Found ... ")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("MMMM")
        return instance


class ProductFeaturedListView(ListView):
    queryset = Product.objects.featured()
    template_name = 'products/list.html'

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/featured_detail.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductDetailView, self).get_context_data(
    #         *args, **kwargs)
    #     print(context)
    #     return context


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(
            *args, **kwargs)
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

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(
            *args, **kwargs)
        print(context)
        return context

    # def get_object(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     instance = Product.objects.get_by_id(pk)
    #     if instance is None:
    #         raise Http404("Product doesn't exist")
    #     return instance

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        return Product.objects.filter(pk=pk)


def products_detail_view(request, pk):
    # instance = Product.objects.get(pk=pk)
    # instance = get_object_or_404(Product, pk=pk)
    # context = {
    #     'object': instance
    # }
    # qs = Product.objects.filter(id=pk)
    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Product doesn't exist")
    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404("Product doesn't exist")
    context = {
        "object": instance
    }
    return render(request, 'products/detail.html', context)
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

    def get_context_data(self, **kwargs):
        context = super(
            ProductBySlugDetailView,
            self
        ).get_context_data(**kwargs)

        cart_obj, new_obj = Cart.objects.get_or_new(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        try:
            instance = Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            raise Http404("Not Found ")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug)
            instance = qs.first()
        except:
            raise Http404("We don't know")
        return instance
