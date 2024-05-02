from django.shortcuts import render
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Count
from django.contrib.auth.models import User
from django.contrib.auth.forms import *

# Create your views here.
def create_user(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, "Registration successfull")
            return redirect(reverse('product_list') + '?category=all')
        else:
            messages.error(request, "Username already exists or password did not meet requirements.")
            return redirect('login')
    else:
        
        form = UserCreationForm()
        return render(request, "account/account.html", {
        'form':form,
        })
    
def login_user(request):
    attempts_count=0
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been authenticated and successfully logged in.")
            return redirect('/All/')
        else:
            messages.success(request, "This username or password is incorrect.")
            attempts_count+=1
            return redirect("login")
    else:
        return render(request, "account/login.html", {})
    
def logout_user(request):
    logout(request)
    messages.success(request, "You have been successfully logged out")
    return redirect('login')