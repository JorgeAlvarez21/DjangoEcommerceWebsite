import ipywidgets
from django import forms
import datetime as dt
from .models import ProductInformation
from . import funcs_content
from Products.funcs_content import categories_names


class QuantityForm(forms.Form):
    quantity = forms.IntegerField(initial=1, required=False, label="")


class AddProductForm(forms.ModelForm):
    class Meta:
        model = ProductInformation
        fields = "__all__"

    category = forms.ChoiceField(choices=funcs_content.categories_names.items(),
                                 required=False,
                                 initial="All Categories",
                                 label=""
                                 )

    def clean_category(self):
        category = self.cleaned_data.get('category')
        return category

