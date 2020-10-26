from django.shortcuts import render
from django.http import HttpResponse #for routing
# Create your views here.

#to create view for test
def home(request):
    return HttpResponse('home')

def product(request):
    return HttpResponse('product')
