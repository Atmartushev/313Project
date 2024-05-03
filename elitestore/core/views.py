
from pyexpat.errors import messages
from django.shortcuts import render
from django.views.generic import ListView
from .models import Category, Product, ProductVariation, Career
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from cart.models import Cart, CartItem
from .forms import SearchForm
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')

# Product views
class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    

    def get_queryset(self):
        self.filter = self.kwargs['filter']
        if self.filter=='All':
            return Product.objects.all()
        else:
            return Product.objects.filter(
                Q(sport__name__iexact=self.filter) | Q(category__name__iexact=self.filter)
            )
        
def product_detail(request, pk):
    if request.user.is_authenticated:
        categories = Category.objects.all()
        product = get_object_or_404(Product, pk=pk)
        product_variations = ProductVariation.objects.filter(product=product)
        colors = set(pv.color for pv in product_variations)
        sizes = set(pv.size for pv in product_variations)

        if request.method == 'POST':
            color = request.POST.get('color')
            size = request.POST.get('size')
            quantity = request.POST.get('quantity')
        
            product_variation = ProductVariation.objects.filter(product=product, color=color, size=size).first()

            if product_variation:
                cart, _ = Cart.objects.get_or_create(user_profile=request.user)
                cart_item, created = CartItem.objects.get_or_create(cart=cart, product_variation=product_variation)
            
                if cart_item:
                    cart_item.quantity += int(quantity)
                    cart_item.save()
                else:
                    CartItem.objects.create(cart=cart, product_variation=product_variation, quantity=1)

                messages.success(request, "Item added to cart.")
                return redirect(request.path)
            else:
                messages.success(request, "Item is out of stock.")
                return redirect(request.path)

        context = {
            'product': product,
            'categories': categories,
            'product_variations': product_variations,
            'colors': colors,
            'sizes': sizes,
        }

        return render(request, 'product_detail.html', context)
    else:
        return redirect('login')

def our_story(request):
    return render(request, 'our_story.html')

def meet_team(request):
    return render(request, 'meet_team.html')

class CareerListView(ListView):
    model = Career
    template_name = 'career_list.html'
    
    def get_queryset(self):
        return Career.objects.all()

def career_detail(request, pk):
    career = Career.objects.get(pk=pk)
    context = {
        'career': career,
    }
    return render(request, 'career_detail.html', context)

def search(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        querytext = request.GET.get('q')
        results = Product.objects.filter(name__icontains=query)
        return render(request, 'search_results.html', {'form': form, 'results': results, 'query': query})
    else:
        return render(request, 'search_results.html', {'form': form})