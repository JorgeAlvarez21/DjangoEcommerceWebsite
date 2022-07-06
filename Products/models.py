from django.db import models



# Create your models here.
class ProductInformation(models.Model):
    name = models.CharField(max_length=30, null=False)
    category = models.CharField(max_length=30)
    price = models.FloatField(null=False)
    on_discount = models.BooleanField(null=True, default=0)
    description = models.TextField(null=True)
    last_modified = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/", null=True)

    def __str__(self):
        return self.name