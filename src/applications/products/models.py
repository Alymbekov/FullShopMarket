from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from .utils import (
    upload_image_path, unique_slug_generator
    )

# ORM - OBJECT RELATIONAL MAPPING

class Product(models.Model):
    slug = models.SlugField(null=True, blank=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=29.99)
    image = models.ImageField(
        upload_to=upload_image_path, null=True, blank=True
    )
    
    def __str__(self):
        return self.title

    def __repr__(self):
        return f'{self.__class__} - {self.title}'


    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         print(self)
    #         self.slug = unique_slug_generator(self)
    #
    #     return super(Product, self).save(*args, **kwargs)


@receiver(signals.pre_save, sender=Product)
def add_product_slug(sender, instance, **kwargs):
    if not instance.id:
        instance.slug = unique_slug_generator(instance)