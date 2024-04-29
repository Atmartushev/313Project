from django.db import models
from account.models import UserProfile
from core.models import ProductVariation

class Cart(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    product = models.ManyToManyField(ProductVariation)

    def total_price(self):
        return sum(product.price for product in self.products.all())
