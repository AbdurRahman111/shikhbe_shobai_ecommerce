from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"), # "" = base url 
    path("product-details/<str:product_slug>/", views.product_details, name="product_details"),

    path('help/', views.help_func, name="help_func"),
    path('support/', views.support_func, name="support_func"),
    path('contact-us/', views.contact_us_func, name="contact_us_func"),
    path('best-seller/', views.best_seller_func, name="best_seller_func"),
    path('cart_page_func/', views.cart_page_func, name="cart_page_func"),
    path('checkout_func/', views.checkout_func, name="checkout_func"),
    path('shop_func/', views.shop_func, name="shop_func"),
]