import ipywidgets
from django import forms
import datetime as dt

import Customers.models
from .models import CustomerInformation
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field


# class CustomerSignupInformation(forms.Form):
#     full_name = forms.CharField(max_length=50, required=True, label= "Full name")
#     email = forms.CharField(max_length=50, required=True, label="email")
#     password = forms.CharField(max_length=50, required=True, label="Password ")
#     password_repeat = forms.CharField(max_length=30, required=True, label="Repeat password ")
#     agreement = forms.BooleanField()


class CustomerSignupVerification(forms.Form):
    agreement = forms.BooleanField(required=False, label="")
    password_repeat = forms.CharField(widget=forms.PasswordInput(), empty_value="blank")

    def clean_password_repeat(self, *args, **kwargs):
        global password_rep_verify
        password_rep_verify = self.cleaned_data.get('password_repeat')
        return password_rep_verify


class CustomerSignupInformation(forms.ModelForm):
    global customer_list

    customer_list = Customers.models.CustomerInformation.objects.all()
    email = forms.EmailField(empty_value=None)
    username = forms.CharField(empty_value=None)
    password = forms.CharField(widget=forms.PasswordInput(), empty_value=None)
    transaction_id = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = CustomerInformation
        fields = "__all__"

    def clean_username(self, *args, **kwargs):
        username_entered = self.cleaned_data.get('username')
        if username_entered == None:
            raise forms.ValidationError('Please enter your username')
        elif customer_list.filter(username=username_entered):
            raise forms.ValidationError('Username already exists')

        return username_entered

    def clean_email(self, *args, **kwargs):
        email_entered = self.cleaned_data.get('email')
        if email_entered == None:
            raise forms.ValidationError('Please enter your email')
        elif customer_list.filter(email=email_entered):
            raise forms.ValidationError('Account already exists for this email')
        return email_entered

    def clean_password(self, *args, **kwargs):
        password_entered = self.cleaned_data.get('password')
        password_rep_entered = self.cleaned_data.get('password_repeat')
        if password_entered == None:
            raise forms.ValidationError('Please enter your password')
        elif password_entered != password_rep_verify:
            raise forms.ValidationError('Password entries should match')
        return password_entered


class CustomerLogin(forms.Form):
    username = forms.CharField(empty_value=None)
    password = forms.CharField(widget=forms.PasswordInput(), empty_value=None)

    def clean_username(self, *args, **kwargs):
        username_entered = self.cleaned_data.get('username')
        verified = customer_list.filter(username=username_entered)
        if verified:
            return username_entered
        else:
            forms.ValidationError('Your username or password is incorrect')

    def clean_password(self, *args, **kwargs):
        password_entered = self.cleaned_data.get('password')
        verified = customer_list.filter(password=password_entered)
        if verified:
            return password_entered
