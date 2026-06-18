"""
==========================================================
VIEWS.PY (accounts app)
==========================================================
Signup creates a new user account. Login/logout use Django's
built-in auth views (wired up in urls.py) so we don't need to
write password-checking logic ourselves -> Django handles that
securely (hashing, session creation, etc.).
"""

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import SignUpForm


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)   # log them in right away after signup
            messages.success(request, f'Welcome, {user.username}! Your account is ready.')
            return redirect('dashboard')
    else:
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form': form})
