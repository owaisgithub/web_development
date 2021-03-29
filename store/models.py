from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    category_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.category_name

    
class Product(models.Model):
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='pics')
    product_name = models.CharField(max_length=200)
    product_discription = models.TextField()
    product_price = models.IntegerField()

    def __str__(self):
        return self.product_name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ordered_date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transation_id = models.CharField(max_length=12)

    def __str__(self):
        return str(self.id)

    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product.name

    def get_total(self):
        total = self.product.product_price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    mobile_number = models.IntegerField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    pin = models.IntegerField()

    def __str__(self):
        return self.address

