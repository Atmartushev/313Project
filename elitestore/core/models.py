from django.db import models
from .models import Cart

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')

class Color(models.Model):
    name = models.CharField(max_length=50)
    hex_value = models.CharField(max_length=7, blank=True, null=True)  # For web color representation

class Size(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)  # Additional details, if needed

class ProductVariation(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock = models.IntegerField()

    class Meta:
        unique_together = ('product', 'color', 'size')  # Ensures each combination is unique

    def __str__(self):
        return f"{self.product.name} - {self.color.name} - {self.size.name}"
