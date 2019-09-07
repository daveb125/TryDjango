from django.http import HttpResponse
from django.shortcuts import render
# from ..profiles.models import Profile
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
    my_context = {                      #sending data to the page as vars to be used in html
        "my_text" : "this is about me",
        "my_number" : 123,
        "my_list" : [123,1,2,3]
    }
    # obj = Profile.objects.get(id=1) #sending data to the page as obj to be used in html done in profiles/views instead
    # context = {
    # "object" : obj
    # }
    return render(request,"login.html",my_context)

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

#Register
def register_view(request,*args,**kwargs):
    return render(request,"register.html",{})