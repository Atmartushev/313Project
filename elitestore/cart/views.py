from pyexpat.errors import messages
from urllib import request
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cart, CartItem
from core.models import ProductVariation, Product, Color, Size

# Create your views here.
def cart_items_view(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Retrieve the user's cart
        user_cart = request.user.cart

        # Retrieve all cart items related to the user's cart
        cart_items = CartItem.objects.filter(cart=user_cart)

        # Pass the cart items to the template for rendering
        context = {'cart_items': cart_items}
        return render(request, 'cart.html', context)
    else:
        # Handle the case where the user is not authenticated
        return render(request, 'login.html')