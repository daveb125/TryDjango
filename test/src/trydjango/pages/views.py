from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Place to handle page creation

#HomePage
def home_view(*args,**kwargs):
    return HttpResponse("<h1>Home</h1>") # string of HTML code

#Login
def login_view(*args,**kwargs):
    return HttpResponse("<h1>Login</h1>") 

#Profile
def profile_view(*args,**kwargs):
    return HttpResponse("<h1>Profile</h1>") 

#BuyCover
def buycover_view(*args,**kwargs):
    return HttpResponse("<h1>BuyCover</h1>") 

#YourCover
def yourcover_view(*args,**kwargs):
    return HttpResponse("<h1>YourCover</h1>") 

#Help
def help_view(*args,**kwargs):
    return HttpResponse("<h1>Help</h1>") 