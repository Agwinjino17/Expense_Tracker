"""
==========================================================
FORMS.PY (expenses app)
==========================================================
A ModelForm auto-generates form fields from the Expense model,
so we don't have to write each <input> field by hand AND get
free validation (e.g. amount must be a number).
"""

from django import forms
from .models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'amount', 'category', 'date', 'notes']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'e.g. Lunch at canteen'}),
            'amount': forms.NumberInput(attrs={'placeholder': '0.00', 'step': '0.01'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Optional note'}),
        }
