from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', include('cart.urls')),
    path('', include('account.urls')),
    
    path('product_detail/<int:pk>/', views.product_detail, name='product_detail'),
    path('<str:category_name>/', views.ProductListView.as_view(), name='product_list'),
]

