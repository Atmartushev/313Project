
from pyexpat.errors import messages
from urllib import request
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Category, Product, Color, Size, ProductVariation
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from cart.models import Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



# Create your views here.
def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects

    # Render the HTML template index.html with the data in the context variable.
    return render(request, 'index.html', {'load_bootstrap': False})


# Product views
class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        if category_name=='All':
            return Product.objects.all()
        else:
            return Product.objects.filter(category__name__iexact=category_name)
        

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    colors = Color.objects.all()
    sizes = Size.objects.all()
    context = {
        'product': product,
        'colors': colors,
        'sizes': sizes,
    }

    if request.method == 'POST':
        color = request.POST.get('color')
        size = request.POST.get('size')
        # Check if color and size are provided
        if color and size:
            # Find the corresponding color and size objects
            color_obj = get_object_or_404(Color, name=color)
            size_obj = get_object_or_404(Size, name=size)
            
            # Create or get the product variation
            product_variation, _ = ProductVariation.objects.get_or_create(
                product=product,
                color=color_obj,
                size=size_obj
            )

            # Create or get the cart associated with the user
            cart, _ = Cart.objects.get_or_create(user_profile=request.user)

            # Check if the cart item already exists
            cart_item = CartItem.objects.filter(cart=cart, product_variation=product_variation).first()

            if cart_item:
                # If the cart item already exists, increase its quantity by 1
                cart_item.quantity += 1
                cart_item.save()
            else:
                # If the cart item does not exist, create it
                cart_item = CartItem.objects.create(
                    cart=cart,
                    product_variation=product_variation,
                    quantity=1
                )

            messages.success(request, "Item added to cart.")
            return redirect('index')  # Redirect to the product list page

    return render(request, 'product_detail.html', context)
