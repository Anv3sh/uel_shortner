from django.shortcuts import render,redirect
import requests
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User

def register(request):
    try:
        if request.method=="POST":
            user=User.objects.create_user(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])

            context={
                'message':'user registered successfully',
            }
            messages.success(request,f'Account created for {user.username}!')
            return redirect('register')
    except:
        messages.success(request,f'user already exists!')
        return redirect('register')

    return render(request,"users/register.html")

def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.success(request,f'username or password not correct!')
    return render(request,'users/login.html')
    