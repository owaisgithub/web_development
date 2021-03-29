from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import ProductCategory, Product, ShippingAddress


def index(request):
    products_category = ProductCategory.objects.all()
    context = {'products_category':products_category}
    return render(request, 'index.html', context)


def productList(request, id):
    try:
        products = ProductCategory.objects.get(pk=id)
    except ProductCategory.DoesNotExist:
        raise Http404("Products Does not exist")
    return render(request, 'productList.html', {'products':products})


def order(request):
    return render(request, 'order.html')

def wallet(request):
    return render(request, 'wallet.html')

def cart(request):
    return render(request, 'cart.html')

def yourAccount(request):
    return render(request, 'yourAccount.html')

def shippingAddress(request):
    if request.method == 'POST':
        name = request.POST["name"]
        mobile_number = request.POST["number"]
        address = request.POST["address"]
        city = request.POST["city"]
        pin = request.POST["pin"]
        
        shipping_address = ShippingAddress.objects.create_user(name=name, mobile_number=mobile_number, address=address, city=city, pin=pin)
        shipping_address.save()

        print("Address is saved!")
        return render(request, 'success.html')

    else:
        return render(request, 'addressForm.html')