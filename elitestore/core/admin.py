from django.contrib import admin
from .models import Product, Category, Size, Color, ProductVariation, Career


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(ProductVariation)
admin.site.register(Career)