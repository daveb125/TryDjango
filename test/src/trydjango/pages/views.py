from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Place to handle page creation

#HomePage
def home_view(request,*args,**kwargs):
    print(args,kwargs)  #empty for now
    print(request.user) #jeremy user for db
    #return HttpResponse("<h1>Home</h1>") # string of HTML code
    return render(request,"home.html",{})

#Login
def login_view(request,*args,**kwargs):
    return render(request,"login.html",{})

#Profile
def profile_view(request,*args,**kwargs):
    return render(request,"profile.html",{})

#BuyCover
def buycover_view(request,*args,**kwargs):
    return render(request,"buycover.html",{})

#YourCover
def yourcover_view(request,*args,**kwargs):
    return render(request,"yourcover.html",{})

#Help
def help_view(request,*args,**kwargs):
    return render(request,"help.html",{})