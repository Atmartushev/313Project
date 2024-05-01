from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('cart', views.CartListView.as_view(), name='cart'),
    path('product_detail/<int:pk>/', views.AddToCart, name='AddToCart'),
]

