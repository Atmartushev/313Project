from django.db import models
from django.contrib.auth.models import User
from cart.models import Cart

class Orders(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)