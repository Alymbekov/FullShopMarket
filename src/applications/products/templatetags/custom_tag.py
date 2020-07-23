from django import template
from applications.products.models import Product

register = template.Library()


@register.simple_tag
def get_featured_products():
    return Product.objects.featured()


@register.inclusion_tag('results.html')
def get_some_results(number):
    print(number)
    print("okay")
    data = [x for x in range(number)]
    return {'data': data}


@register.filter
def swapcase(value):
    return value.swapcase()
