from django.shortcuts import render,redirect
from django.urls import path, include
from .views import login, register
urlpatterns=[
    path('register/',register,name="register"),
    path('login/',login,name="login"),

]