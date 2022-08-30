from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('single_product/<int:productId>/',views.single_product,name='single_product'),
    
    path("register", views.register, name= "register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),


]