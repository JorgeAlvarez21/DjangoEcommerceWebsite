from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from Cart.models import ShoppingCart
from Products.models import ProductInformation
from . import func_tools
from .forms import *


# Create your views here.


def shoppingCart(request):
    user = request.user
    qty_edit_form = ShoppingQtyForm()
    payment_info_form = UserPaymentForm()

    products = ProductInformation.objects.all()
    cart_items = ShoppingCart.objects.all().filter(user_username=user)
    total_amount = 0
    if len(cart_items) > 0:
        user_transaction_id = cart_items[0].user_transaction_id
        total_amount = func_tools.cartTotal(user_transaction_id)

    if request.method == 'POST':
        form = ShoppingQtyForm(request.POST)
        prod_id_remove = request.POST.get("remove-btn")
        prod_id_save = request.POST.get("save-btn")

        if form.is_valid():
            new_qty = form.cleaned_data['quantity_edited']

            if prod_id_remove is not None:
                func_tools.UserCart(user).DeleteProduct(prod_id=prod_id_remove)
            elif prod_id_save is not None:
              func_tools.UserCart(user).UpdateQuantity(prod_id=prod_id_save, add_qty=new_qty)

        return redirect('shopping-cart')







    context = {'cart_items': cart_items, 'products': products, 'total_amount': total_amount,
               'qty_edit_f': qty_edit_form, 'payment_info_f': payment_info_form}

    return render(request, 'shoppingCartTemp.html', context)

