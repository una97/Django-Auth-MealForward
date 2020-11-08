#routing folder -> called from mf_auth folder
from django.urls import path
from . import views # from base '.'

urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name ="home"), # base url with 'views'.home function 
    path('user/', views.userPage, name="user-page"),
    path('products/', views.products,name="products"),
    path('customer/<str:pk_test>', views.customer,name="customer")

]

