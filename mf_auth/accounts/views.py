from django.shortcuts import render, redirect
from django.http import HttpResponse #for routing
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group ##need to be added

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import * #to import model
from .forms import OrderForm, CreateUserForm
from .decorators import *
#to create view for test
@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='restaurant')
            user.groups.add(group)

            messages.success(request, 'Account ' + username)

            return redirect('login')
    context = {
        'form' :form
    }
    return render(request, 'accounts/register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

@unauthenticated_user
def loginPage(request):
    if request.user.is_authenticated:
	    return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)

@login_required(login_url='login')
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    
    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders':orders, 'customers':customers,
	'total_orders':total_orders,'delivered':delivered,
	'pending':pending }

    # return HttpResponse('home')
    return render(request,'accounts/dashboard.html',context)

@allowed_users(allowed_roles=['restaurant'])
def userPage(request):
    context = {}
    return render(request, 'accounts/user.html', context)

@login_required(login_url='login')
def products(request):
    products = Product.objects.all()
    return render(request,'accounts/products.html',{'products':products})

@login_required(login_url='login')
def customer(request,pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all() # it grabs all orders with specific customer
    order_count = orders.count()

    context = {
        'customer' : customer,
        'orders' : orders,
        'order_count' : order_count
    }
    return render(request,'accounts/customer.html',context)

