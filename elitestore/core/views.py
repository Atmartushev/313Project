
from pyexpat.errors import messages
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Product, Color, Size, ProductVariation, Career
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from cart.models import Cart, CartItem



# Create your views here.
def index(request):
    return render(request, 'index.html')

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
    categories = Category.objects.all()
    product = get_object_or_404(Product, pk=pk)
    colors = Color.objects.all()
    sizes = Size.objects.all()
    context = {
        'product': product,
        'colors': colors,
        'sizes': sizes,
        'categories': categories,
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
            return redirect(request.path)  # Redirect to the product list page
    return render(request, 'product_detail.html', context)

def our_story(request):
    return render(request, 'our_story.html')

def meet_team(request):
    return render(request, 'meet_team.html')

def career_list(request):
    career = Career.objects.all()
    context = {
        'career_list': career,
    }
    return render(request, 'career_list.html', context)

def career_detail(request, pk):
    career = Career.objects.get(pk=pk)
    context = {
        'career': career,
    }
    return render(request, 'careers.html', context)