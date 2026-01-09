from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup_func, name="signup_func"),
]