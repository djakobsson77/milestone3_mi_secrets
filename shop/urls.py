from django.urls import path
from . import views

urlpatterns = [
    path("", views.shop, name="shop"),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:game_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:item_id>/', views.update_cart, name='update_cart'),
    path(
        'cart/remove/<int:item_id>/',
        views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
]
