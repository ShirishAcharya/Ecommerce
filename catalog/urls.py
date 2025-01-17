from django.contrib import admin
from django.urls import path,include
from catalog import views

urlpatterns = [
    path("",views.home,name='home'),
    path("signup/",views.user_signup,name="user_signup"),
    path("login/",views.user_login,name="user_login"),
    path("logout/",views.user_logout,name="user_logout"),
    path("my/cart/",views.cart_detail,name="cart_detail"),
    path('product/<int:id>/',views.product_detail,name="product_detail"),
    path('add/to/cart/<int:id>/',views.add_to_cart,name="add_to_cart"),	
    path("create/product/",views.create_product,name='create_product'),
    path("list/product",views.list_product,name='list_product'),
    path("update/product/<int:id>/",views.update_product,name='update_product'),
]