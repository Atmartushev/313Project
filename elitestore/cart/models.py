from django.db import models
from core.models import ProductVariation
from django.contrib.auth.models import User

class Cart(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE)

    def total_price(self):
        return sum(item.product_variation.price * item.quantity for item in self.cartitem_set.all())
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_variation = models.ForeignKey(ProductVariation, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product_variation} (Quantity: {self.quantity})"