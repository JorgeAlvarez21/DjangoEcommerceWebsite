from django.db import models

# Create your models here.


class CustomerInformation(models.Model):
    username = models.CharField(max_length=50, null=False, default='')
    full_name = models.CharField(max_length=100, null=False, default='')
    email = models.CharField(max_length=100, null=False, default='')
    password = models.CharField(max_length=30, null=False, default='')
    transaction_id = models.CharField(max_length=30, null=True)



    def __str__(self):
        return str(self.full_name)