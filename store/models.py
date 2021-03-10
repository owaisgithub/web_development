from django.db import models


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

