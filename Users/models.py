from django.db import models

# Create your models here.
class UserInformation(models.Model):
    username = models.CharField(max_length=12)
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    birthdate = models.DateField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name_first, self.name_last, self.username
