from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup_func, name="signup_func"),
    path('login/', views.login_func, name="login_func"),
    path('logout/', views.logout_func, name="logout_func"),
    path('my_profile/', views.my_profile, name="my_profile"),
    # path('forgot_password/', views.forgot_password, name="forgot_password"),

    path('password-reset/', views.custom_password_reset, name='password_reset'),
    path('reset/<uidb64>/<token>/', views.custom_password_reset_confirm, name='password_reset_confirm'),
]