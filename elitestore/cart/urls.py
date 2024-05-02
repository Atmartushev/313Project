from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('mycart', views.cart_items_view, name='cart'),
]

