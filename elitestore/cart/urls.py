from django.urls import path
from . import views


urlpatterns = [
    path('mycart/', views.cart_items_view, name='cart'),
    path('delete_cart_item/<int:pk>', views.delete_cart_item, name="delete_cart_item"),
    path('update_cart/<int:pk>', views.update_cart, name="update_cart"),
    path('create_order/', views.create_order, name='create_order')
]

