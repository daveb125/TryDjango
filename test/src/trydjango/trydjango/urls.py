"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pages.views import home_view,buycover_view,yourcover_view,help_view,login_view,profile_view,register_view

urlpatterns = [
    #Home
    path('',home_view, name='home'),
    path('home/',home_view, name='home'),
    #Your Profile
    path('profile/',profile_view, name='profile'),
    #Buy Cover
    path('buycover/',buycover_view, name='buycover'),
    #Your Cover
    path('yourcover/',yourcover_view, name='yourcover'),
    #Help
    path('help/',help_view, name='help'),
    #Login  
    path('login/',login_view,name='login'),
    #Admin panel
    path('admin/', admin.site.urls),
    #Register
    path('register/',register_view,name='register'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

