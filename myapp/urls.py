from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.login, name='login'),
    path("login", views.login, name='login'),
    path("logout", views.logout, name='logout'),
    path("home", views.home, name='home'),
    path("contact", views.contact, name='contact'),
    path("profile", views.profile, name='profile'),
]
