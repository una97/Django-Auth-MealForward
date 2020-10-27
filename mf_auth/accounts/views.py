from django.shortcuts import render
from django.http import HttpResponse #for routing
# Create your views here.

from .models import * #to import model

#to create view for test
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
def products(request):
    products = Product.objects.all()
    return render(request,'accounts/products.html',{'products':products})
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

