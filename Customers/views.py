from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from Customers import forms, func_tools
from Customers.models import CustomerInformation as customer
from django.contrib.auth.models import User


# Create your views here.

def signupScreen(request):
    customer_info_form = forms.CustomerSignupInformation()
    customer_verify_form = forms.CustomerSignupVerification()

    if request.method == 'POST':
        customer_info_form = forms.CustomerSignupInformation(request.POST)
        customer_verify_form = forms.CustomerSignupVerification(request.POST)
        if customer_verify_form.is_valid():
            if customer_verify_form.cleaned_data.get("agreement"):
                password_verify = customer_verify_form.cleaned_data.get("password_repeat")
                if customer_info_form.is_valid():
                    username = customer_info_form.cleaned_data.get("username")
                    name = customer_info_form.cleaned_data.get("full_name")
                    email = customer_info_form.cleaned_data.get("email")
                    password = customer_info_form.cleaned_data.get("password")
                    trans_id = func_tools.generate_TransID()
                    new_user =  customer(username=username, full_name=name, email=email, password=password, transaction_id=trans_id)
                    new_user.save()
                    user = User.objects.create_user(username=username, email = email, password=password)
                    user_auth = authenticate(request, username=username, password=password)
                    #redirect to youi account has been created please log in, in login template
                    if user_auth is not None:
                        login(request, user_auth)
                        redirect('Homepage')
                        #fix username no spaces
        #fix raise value error agreement


    context = {"customer_info_f": customer_info_form, "customer_verify_f": customer_verify_form}

    return render(request, 'signupTemp.html', context)



# user = User.objects.create_user(username='Niraj',
#                                  email='deyneeraj612.com',
#                                  password='glass onion')
def loginScreen(request):
    login_form = forms.CustomerLogin()
    if request.method == 'POST':
        form = forms.CustomerLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user_authenticate = authenticate(request, username=username, password=password)
            if user_authenticate is not None:
                login(request, user_authenticate)
                return HttpResponseRedirect("/homepage/")
    context = {'login_f': login_form}
    return render(request, 'loginTemp.html', context)

def logoutScreen(request):
    if 'proceed_to_logout' in request.POST:
        logout(request)
        return HttpResponseRedirect("/homepage/")

    return render(request, 'logoutTemp.html')


def Base(request):
    return render(request, 'Base.html')


