"""
==========================================================
URLS.PY (accounts app)
==========================================================
Signup is our own custom view. Login/logout reuse Django's
built-in auth views -> LoginView and LogoutView already handle
password checking, session creation, and redirects securely.
"""

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
