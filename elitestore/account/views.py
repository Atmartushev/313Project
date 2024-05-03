from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import *
from cart.models import Cart, CartItem
from .models import Orders

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
      cart = Cart.objects.get(user_profile=request.user)
      cart_items = CartItem.objects.filter(cart=cart)
      orders = Orders.objects.filter(user=request.user)

      total_price = 0
      for item in cart_items:
        item_total = item.quantity * item.product_variation.product.price
        item.item_total = item_total  # Add item_total attribute to the item object
        total_price += item_total

    # Convert cart_items to a list to allow adding attributes dynamically
    cart_items_list = list(cart_items)
    # Add item_total attribute to each item object in the list
    for item in cart_items_list:
        item.item_total = item.quantity * item.product_variation.product.price

    context = {'cart_items': cart_items, 
                   'total_price': total_price,
                   'cart': cart,
                   'orders': orders}
    return render(request, "account.html", context)
    else:
        return redirect('login')
