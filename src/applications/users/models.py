from django.db import models
from django.contrib.auth.models import User  
from applications.products.utils import upload_image_path

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles')
    avatar = models.ImageField(upload_to=upload_image_path, blank=True)
    full_name = models.CharField(max_length=100, blank=True)
    age = models.PositiveSmallIntegerField(default=18)


    def __str__(self):
        return self.user.username
