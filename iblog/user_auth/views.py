from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def user_login(request):
        if request.method == 'POST' and 'login' in request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home or any other page after login
            else:
                messages.error(request, 'Invalid email or password.')
        return render(request, 'login.html')

def user_signup(request):
    if request.method == 'POST' and 'signup' in request.POST:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email is already taken.')
        else:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = username
            user.save()
            messages.success(request, 'Account created successfully. Please login.')
            return redirect('auth')  # Redirect to the same page to login
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('auth')