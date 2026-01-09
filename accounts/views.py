from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.


def signup_func(request):
    if request.method == 'POST':
        print("Submitted signup form ...")

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Password does not match!")
            return redirect('signup_func')

        if User.objects.filter(username  = username).exists():
            messages.error(request, "Username Already Exists!")
            return redirect('signup_func')

        if User.objects.filter(email = email).exists():
            messages.error(request, "Email Already Exists!")
            return redirect('signup_func')
        

        user = User.objects.create_user(
            username = username,
            email = email, 
            password = password,
            first_name=first_name,
            last_name=last_name,
        )
        user.save()

        messages.success(request, "Account Created Successfully!")
        return redirect('signup_func')
    else:
        return render(request, "signup_page.html")