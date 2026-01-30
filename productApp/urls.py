from django.urls import path
from . import views

app_name='productApp'

urlpatterns = [
    path("add-to-cart/", views.add_to_cart_ajax, name="add_to_cart_ajax")
]