from rest_framework import serializers
from .models import ProductInformation


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInformation
        fields = '_all_'


