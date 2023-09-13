from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Product, Tag
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    tags = Tag.objects.get(slug='featured')
    featured_products = Product.objects.filter(tags=tags)
    # print(featured_products)
    return render(request, 'home.html', {
        "featured_products": featured_products
    })

def store(request):
    items_per_page = 9
    products_q = Product.objects.filter(active=True)
    sort = request.GET.get('sort', None)
    if sort == 'featured':
        products_q = products_q.filter(tags__slug=sort)
    if sort == 'created_at':
        products_q = products_q.order_by('-created_at')

    paginator = Paginator(products_q.all(), items_per_page)
    page_number = request.GET.get('page')  # Get the current page number from the request
    products = paginator.get_page(page_number)

    return render(request, 'store.html', {
        'products': products,
    })

def singleProduct(request, slug):
    product = Product.objects.filter(slug=slug).first()

    return render(request, 'single-item.html', {'product': product})
