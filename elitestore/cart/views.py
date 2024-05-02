from pyexpat.errors import messages
from urllib import request
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cart, CartItem
from core.models import ProductVariation, Product, Color, Size

# Create your views here.
class CartListView(ListView):
    model = CartItem
    template_name = 'cart.html'
    context_object_name = 'cart_item'
