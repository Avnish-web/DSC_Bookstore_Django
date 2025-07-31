from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Book

@login_required(login_url='login')
def home(request):
    books = Book.objects.all().order_by('-created_at')[:5]
    return render(request, 'bookstore/home.html', {'books': books})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')

        if not username:
            return render(request, 'bookstore/login.html', {'error': 'Username is required'})

        # Get or create a user with no password
        user, created = User.objects.get_or_create(username=username)
        user.set_unusable_password()  # Prevent password-based login
        user.save()

        auth_login(request, user)  # Log in user without password
        return redirect('home')

    return render(request, 'bookstore/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
