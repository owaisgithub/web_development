from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:id>/', views.productList, name="productList"),
    path('order_details/', views.order, name='order'),
    path('wallet/', views.wallet, name='wallet'),
    path('cart/', views.cart, name='cart'),
    path('your_account_detail', views.yourAccount, name='yourAccount'),
    path('category/products/', views.shippingAddress, name="addressForm"),
    path('success/', views.shippingAddress, name="shippingAddress"),
    path('update_items', views.updateItems, name='updateItems'),
]