"""
==========================================================
FORMS.PY (accounts app)
==========================================================
Django ships UserCreationForm out of the box (username + password
+ confirm password, with built-in validation). We just add an
email field on top since the default form doesn't include one.
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
