from django.db import models
from .utils import (
    upload_image_path, unique_slug_generator
    )

from django.http import Http404


# ORM - OBJECT RELATIONAL MAPPING

class FeaturedQuerySet(models.QuerySet):
    def featured(self):
        return self.filter(is_featured=True)
        
class ProductManager(models.Manager):
    def get_queryset(self):
        return FeaturedQuerySet(self.model, using=self._db)
    
    def featured(self):
        return self.get_queryset().featured()

    def get_by_id_s(self, pk):
        obj = Product.objects.filter(pk=pk)
        if obj.exists and obj.count() == 1:
            obj = obj.first()
        else:
            raise Http404("Нет такой id для продукта")
        return obj
        
class Product(models.Model):
    slug = models.SlugField(null=True, blank=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=29.99)
    is_featured = models.BooleanField(default=False)
    image = models.ImageField(
        upload_to=upload_image_path, null=True, blank=True
    )
    objects = ProductManager()
    
    def __str__(self):
        return self.title

    def __repr__(self):
        return f'{self.__class__} - {self.title}'


    def save(self, *args, **kwargs):
        if not self.id:
            print(self)
            self.slug = unique_slug_generator(self)

        return super(Product, self).save(*args, **kwargs)   
