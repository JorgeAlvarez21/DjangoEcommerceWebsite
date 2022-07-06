from django.db import models

# Create your models here.
class OrderInformation(models.Model):
    user_fullname = models.CharField(max_length=30, null=False)
    product_names = models.TextField(null=False)
    total_paid = models.FloatField(null=False)
    card_on_file = models.CharField(max_length=16, null=True)
    card_exp_date = models.DateTimeField(null=True)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_fullname, self.transaction_date
