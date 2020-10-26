from django.shortcuts import render
from django.http import HttpResponse #for routing
# Create your views here.

#to create view for test
def home(request):
    # return HttpResponse('home')
    return render(request,'accounts/dashboard.html')
def products(request):
    return render(request,'accounts/products.html')
def customer(request):
    return render(request,'accounts/customer.html')

