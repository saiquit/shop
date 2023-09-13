from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Product, Tag
# Create your views here.

def home(request):
    tags = Tag.objects.get(slug='featured')
    featured_products = Product.objects.filter(tags=tags)
    # print(featured_products)
    return render(request, 'home.html', {
        "featured_products": featured_products
    })

def store(request):
    return render(request, 'store.html')

def singleProduct(request, slug):
    product = Product.objects.filter(slug=slug).first()

    return render(request, 'single-item.html', {'product': product})