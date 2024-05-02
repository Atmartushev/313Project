from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('product_detail/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('', include('cart.urls')),
    path('our-story/', views.our_story, name = 'our_story'),
    path('meet-the-team/', views.meet_team, name = 'meet_team'),
    path('<str:category_name>/', views.ProductListView.as_view(), name='product_list'),
]

