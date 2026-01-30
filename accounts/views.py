from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
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
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, "signup_page.html")



def login_func(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username)
        print(password)

        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successfully!")
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login_func')

    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, "login_page.html")




def logout_func(request):
    logout(request)
    return redirect('login_func')


@login_required
def my_profile(request):
    return render(request, "my_profile.html")


def forgot_password(request):
    return render(request, "forgot_password.html")



# In your views.py
from django.shortcuts import render, redirect
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.http import HttpResponseBadRequest
import re

# Password Reset Request View
def custom_password_reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        
        # Validate email
        if not email:
            messages.error(request, 'Please enter your email address.')
            return render(request, 'password_reset.html')
        
        # Check if user exists
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # Don't reveal that user doesn't exist for security
            messages.success(request, 'If an account exists with this email, you will receive password reset instructions.')
            return render(request, 'password_reset_done.html')
        
        # Generate token and UID
        token = default_token_generator.make_token(user)
        
        uid = urlsafe_base64_encode(force_bytes(user.id))
        # print(urlsafe_base64_encode(force_bytes(user.id)))
        
        # Build reset URL
        reset_url = request.build_absolute_uri(f'/reset/{uid}/{token}/')

        print(reset_url)
        
        # Email content
        # subject = 'Password Reset Request'
        # message = render_to_string('email/password_reset_email.html', {
        #     'user': user,
        #     'reset_url': reset_url,
        #     'site_name': 'www.example.com',
        # })
        
        # # Send email
        # send_mail(
        #     subject,
        #     message,
        #     settings.DEFAULT_FROM_EMAIL,
        #     [email],
        #     fail_silently=False,
        # )
        
        messages.success(request, 'Password reset email sent successfully!')
        return render(request, 'password_reset_done.html')
    
    return render(request, 'password_reset.html')



# Password Reset Confirm View
def custom_password_reset_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            password1 = request.POST.get('new_password1')
            password2 = request.POST.get('new_password2')
            
            # Custom password validation
            errors = []
            
            if not password1 or not password2:
                errors.append('Please fill in both password fields.')
            
            if password1 != password2:
                errors.append('Passwords do not match.')
            
            if len(password1) < 8:
                errors.append('Password must be at least 8 characters long.')
            
            if not re.search(r'[A-Z]', password1):
                errors.append('Password must contain at least one uppercase letter.')
            
            if not re.search(r'[a-z]', password1):
                errors.append('Password must contain at least one lowercase letter.')
            
            if not re.search(r'\d', password1):
                errors.append('Password must contain at least one digit.')
            
            if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password1):
                errors.append('Password must contain at least one special character.')
            
            if errors:
                for error in errors:
                    messages.error(request, error)
                return render(request, 'password_reset_confirm.html', {'validlink': True})
            
            # Set new password
            user.set_password(password1)
            user.save()
            
            messages.success(request, 'Your password has been reset successfully! You can now login with your new password.')
            return render(request, 'password_reset_complete.html')
        
        return render(request, 'password_reset_confirm.html', {'validlink': True})
    else:
        messages.error(request, 'The password reset link is invalid or has expired.')
        return render(request, 'password_reset_confirm.html', {'validlink': False})

