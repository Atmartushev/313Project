from django.contrib import messages
from urllib import request
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem


def cart_items_view(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Retrieve the user's cart
        cart = Cart.objects.get(user_profile=request.user)
        cart_items = CartItem.objects.filter(cart=cart)

        # Calculate total price for each cart item and total price for the entire cart
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
            
        

        # Pass the cart items, item totals, and total price to the template for rendering
        context = {'cart_items': cart_items, 'total_price': total_price}
        return render(request, 'cart.html', context)
    else:
        # Handle the case where the user is not authenticated
        return render(request, 'login.html')
    
def delete_cart_item(request, pk):
    cart_item = CartItem.objects.get(pk=pk)
    cart_item.delete()
    return redirect('cart')
    
def delete_cart(request):
    cart = Cart.objects.get(user_profile=request.user)
    cart.delete()
    return redirect('index')

def update_cart(request, pk):
    quantity = request.POST.get('quantity')
    if not quantity.isdigit() or int(quantity) <= 0:
        messages.error(request, "Invalid quantity.")
        return redirect('cart')
        
    cart_item = CartItem.objects.get(pk=pk)
    cart_item.quantity = int(quantity)
    cart_item.save()
    messages.success(request, "Cart item quantity updated successfully.")
    return redirect('cart')