from django.shortcuts import render, get_object_or_404
from .models import Product, Store, Category
from django.http import Http404

def index(request):
    products = Product.objects.order_by('-created_at')[:3]
    return render(request, 'index.html', {'products': products})

def product_list(request):
    products = Product.objects.order_by('-created_at')
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product_detail.html', {'product': product})

def store_list(request):
    stores = Store.objects.all()
    return render(request, 'store_list.html', {'stores': stores})

def store_detail(request, slug):
    store = get_object_or_404(Store, slug=slug)
    print("---------------------")
    print(store)
    return render(request, 'store_detail.html', {'store': store})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_product_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.order_by('-created_at')
    return render(request, 'category_product_list.html', {'category': category, 'products': products})

def test_404(request):
    raise Http404("Pàgina no trobada")
