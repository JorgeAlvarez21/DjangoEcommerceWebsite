from django.contrib import admin
from Users.models import UserInformation
from Orders.models import OrderInformation
from Products.models import ProductInformation
# Register your models here.

admin.site.register(UserInformation, ProductInformation, OrderInformation)