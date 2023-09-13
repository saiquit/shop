from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/uploads/products/', blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    variations =models.ManyToManyField("store.Variation", blank=True)

    def __str__(self):
        return self.name

class Variation(models.Model):
    products = models.ForeignKey("store.Product", on_delete=models.CASCADE)
    color = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    def __str__(self):
        return self.size

# Create Slug if not created
@receiver(pre_save, sender=Category)
@receiver(pre_save, sender=Product)
@receiver(pre_save, sender=Tag)
def create_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)