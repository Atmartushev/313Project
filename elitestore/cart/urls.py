from django.urls import path
from . import views


urlpatterns = [
    path('mycart/', views.cart_items_view, name='cart'),
    path('delete_cart/', views.delete_cart, name="delete_cart"),
    path('delete_cart_item/<int:pk>', views.delete_cart_item, name="delete_cart_item"),
    path('update_cart/<int:pk>', views.update_cart, name="update_cart")
]

