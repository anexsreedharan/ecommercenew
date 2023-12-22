from django.urls import path
from . import views

app_name='cart'
urlpatterns=[
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('',views.cart_detail,name='cart_detail'),
    path('remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
    path('full_remove/<int:product_id>/',views.full_remove,name='full_remove'),
    path('cart/pay/',views.payment,name='payment'),
    path('cart/pay/congrats',views.congrats,name='congrats'),
]