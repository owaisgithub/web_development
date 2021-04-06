from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import ProductCategory, Product, ShippingAddress, Order, OrderItem, Customer


def index(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']

    products_category = ProductCategory.objects.all()
    context = {
        'products_category' : products_category,
        'cartItems' : cartItems,
    }
    return render(request, 'index.html', context)


def productList(request, id):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']

    products = ProductCategory.objects.get(pk=id)
    context = {
        'products' : products,
        'cartItems' : cartItems,
    }
    return render(request, 'productList.html', context)

def updateItems(request):
    return HttpResponse('Good!')

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
        
        shipping_address = ShippingAddress(name=name, mobile_number=mobile_number, address=address, city=city, pin=pin)
        shipping_address.save()

        print("Address is saved!")
        return render(request, 'success.html')

    else:
        return render(request, 'addressForm.html')