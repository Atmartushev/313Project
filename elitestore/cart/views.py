from pyexpat.errors import messages
from urllib import request
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cart


# Create your views here.
class CartListView(ListView):
    model = Cart
    template_name = 'cart.html'
    context_object_name = 'cart'

def AddToCart(request, pk):
    
    messages.success(request, "Item Added to cart")