from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html'
    )

def item_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'item_detail.html', {'product': product})
