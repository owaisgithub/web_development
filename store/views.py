from django.shortcuts import render

from .models import ProductCategory, Product


def index(request):
    products_category = ProductCategory.objects.all()
    context = {'products_category':products_category}
    return render(request, 'index.html', context)


def order(request):
    return render(request, 'order.html')

def wallet(request):
    return render(request, 'wallet.html')

def cart(request):
    return render(request, 'cart.html')

def yourAccount(request):
    return render(request, 'yourAccount.html')