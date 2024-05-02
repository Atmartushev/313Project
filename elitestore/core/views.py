
from pyexpat.errors import messages
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Product, ProductVariation
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
    product_variations = ProductVariation.objects.filter(product=product)
    colors = set(pv.color for pv in product_variations)
    sizes = set(pv.size for pv in product_variations)

    if request.method == 'POST':
        color = request.POST.get('color')
        size = request.POST.get('size')
        
        product_variation = ProductVariation.objects.filter(product=product, color=color, size=size).first()

        if product_variation:
            cart, _ = Cart.objects.get_or_create(user_profile=request.user)
            cart_item = CartItem.objects.filter(cart=cart, product_variation=product_variation).first()

            if cart_item:
                cart_item.quantity += 1
                cart_item.save()
            else:
                CartItem.objects.create(cart=cart, product_variation=product_variation, quantity=1)

            messages.success(request, "Item added to cart.")
            return redirect(request.path)
        else:
            messages.success(request, "The selected color and size combination does not exist.")
            return redirect(request.path)

    context = {
        'product': product,
        'categories': categories,
        'product_variations': product_variations,
        'colors': colors,
        'sizes': sizes,
    }

    return render(request, 'product_detail.html', context)



def our_story(request):
    return render(request, 'our_story.html')

def meet_team(request):
    return render(request, 'meet_team.html')
