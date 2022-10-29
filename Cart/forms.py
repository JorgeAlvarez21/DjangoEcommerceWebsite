from django import forms


class ShoppingQtyForm(forms.Form):
    quantity_edited = forms.IntegerField(required=False, initial=1, label="")




class UserPaymentForm(forms.Form):
    card_number = forms.CharField(max_length=16, required=False)
    card_name = forms.CharField(max_length=50, required=False)
    issued_date = forms.DateField(required=False)
    exp_date = forms.DateField(required=False)
    cvv_code = forms.CharField(max_length=3, required=False)



# class UserInformationForm(forms.Form):
