from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args , **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else : 
            return view_func(request, *args , **kwargs)

    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args , **kwargs):
            group = None
            username = request.user.username
            
            if request.user.groups.exists(): #if this user in group
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args , **kwargs)

            else:
                return HttpResponse(username + " is " +group+". SO You are not allowed!!!")
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_func(request, *args , **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'moderator' :
            return view_func(request, *args , **kwargs)
        if group == 'restaurant' :
            return redirect('user-page')
    return wrapper_func