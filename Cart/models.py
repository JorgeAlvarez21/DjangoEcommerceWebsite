from django.db import models


# Create your models here.

class ShoppingCart(models.Model):
    user_username = models.CharField(max_length=50, null=False)
    user_transaction_id = models.CharField(max_length=30, null=False)
    product_id = models.IntegerField(null=False)
    product_name = models.CharField(max_length=100, null=False)
    product_quantity = models.IntegerField(null=True, default=0)
    product_image = models.ImageField(upload_to="prod-images-cart/", null=True)
    product_price = models.FloatField(null=True)
    product_subtotal = models.FloatField(null=True)
    product_description = models.TextField(null=True)
    product_brand = models.CharField(null=True, max_length=20)



