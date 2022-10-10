from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.SignIn , name='SignIn'),
    path("signup/", views.SignUp, name='signup'),
    path("homepage",views.homepage,name='home')
]
