import os

import random
import string

from transliterate import detect_language
from transliterate import slugify as slugify_translit
from django.utils.text import slugify

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    print("Instance", instance)
    print("Filename", filename)
    new_filename = random.randint(666666, 399999999)
    name, ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f'products/{new_filename}/{final_filename}'

def random_slug_generator(
    size=10, 
    chars=string.ascii_lowercase \
        + string.digits):
        return "".join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
    print(new_slug)
    if new_slug is not None:
        slug = new_slug
    else:
        lang = detect_language(instance.title)
        if lang:
            slug = slugify_translit(instance.title, lang)
        else:
            slug = slugify(instance.title, allow_unicode=True)

    Class_ = instance.__class__

    queryset_exists = Class_.objects.filter(slug=slug).exists()
   
    if queryset_exists:
        new_slug = f'{slug}-{random_slug_generator(size=15)}'
        return unique_slug_generator(instance, new_slug=new_slug)
    
    return slug
