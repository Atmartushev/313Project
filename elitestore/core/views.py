
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Category, Product, Color, Size, ProductVariation
from django.shortcuts import render, get_object_or_404


# Create your views here.
def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html'
    )


# Product views
class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

def item_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'item_detail.html', {'product': product})
