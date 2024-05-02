from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('mycart', views.CartListView.as_view(), name='cart'),
]

