from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import *
from cart.models import Cart, CartItem
from account.models import Orders

# Create your views here.
def create_user(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user = authenticate(username = username, password = password, email = email)
            login(request, user)
            messages.success(request, "Registration successfull")
            return redirect(reverse('index'))
        else:
            messages.error(request, "Username already exists or password did not meet requirements.")
            return redirect('login')
    else:
        
        form = UserCreationForm()
        return render(request, "create_user.html", {
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
            return redirect(reverse('index'))
        else:
            messages.success(request, "This username or password is incorrect.")
            attempts_count+=1
            return redirect("login")
    else:
        return render(request, "login.html", {})
    
def logout_user(request):
    logout(request)
    messages.success(request, "You have been successfully logged out")
    return redirect('index')

def account(request):
    if request.user.is_authenticated:
        # Retrieve the user's cart
        cart = Cart.objects.get(user_profile=request.user)
        cart_items = CartItem.objects.filter(cart=cart)

        # Pass the cart items to the template for rendering
        return render(request, 'account.html', {'cart_items': cart_items})
    else:
        return redirect('login')