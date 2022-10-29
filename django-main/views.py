from django.http import HttpResponse

import Orders, Products, Customers
from django.shortcuts import render, redirect
from Products import forms, funcs_content
from Products import models
from Cart import func_tools



def Homepage(request):
    product_items = models.ProductInformation.objects.all()
    categories_items = funcs_content.categories_names
    quantity_form = forms.QuantityForm()


    if request.method == 'GET':
        category_name = request.GET.get('category-btn')

        if category_name:
            category_key = list(categories_items.keys())[list(categories_items.values()).index(category_name)]
            product_items = product_items.filter(category=category_key)

        try:
            search_keyword = request.GET.get('search-bar').lower()
            product_items = funcs_content.search_text(search_keyword, product_items)

            context = {'products_info': product_items, 'dpd_items': categories_items.values(), 'quantity_f':quantity_form}
            return render(request, 'homepage.html', context)
        except Exception as e:
            pass

    if request.method == 'POST':
        cart = func_tools.UserCart(request.user)
        form = forms.QuantityForm(request.POST)
        if form.is_valid():
            product_qty = form.cleaned_data.get('quantity')
        else:
            product_qty = 1
        product_id = request.POST.get('retrieve_id')
        cart.addProduct(product_id, product_qty)


            # func_tools.addToCart(request.user, product_name, product_id)

    context = {'products_info': product_items, 'dpd_items': categories_items.values(), 'quantity_f':quantity_form}

    return render(request, 'homepage.html', context)


def MgmtDashboard(request):
    context = {}
    return render(request, 'mgmtDashTemp.html', context)


def ProductsRegistry(request):
    prod_reg_form = forms.AddProductForm()
    ret_items = models.ProductInformation()
    products = models.ProductInformation.objects.all()

    if request.method == 'POST':
        prod_reg_form = forms.AddProductForm(request.POST, request.FILES)
        if prod_reg_form.is_valid():
            prod_reg_form.save()
            return redirect('Success')
        else:

            prod_reg_form = forms.AddProductForm()


    context = {'reg_form': prod_reg_form, 'products': products}
    return render(request, 'product-register.html', context)


def Success(request):
    return render(request, 'success-temp.html')

