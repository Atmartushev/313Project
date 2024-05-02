from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('cart.urls')),
    path('', include('account.urls')),
    path('product_detail/<int:pk>/', views.product_detail, name='product_detail'),
    path('our-story/', views.our_story, name = 'our_story'),
    path('meet-the-team/', views.meet_team, name = 'meet_team'),
    path('our-careers/', views.CareerListView.as_view(), name = 'career_list'),
    path('our-careers/<int:pk>/', views.career_detail, name = 'career_detail'),
    path('<str:category_name>/', views.ProductListView.as_view(), name='product_list'),
]

