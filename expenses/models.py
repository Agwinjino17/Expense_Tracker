"""
==========================================================
MODELS.PY (expenses app)
==========================================================
Defines the Expense table. Each expense belongs to exactly one
user (ForeignKey to Django's built-in User model), so when we
query expenses for a logged-in user, we only get THEIR rows.
"""

from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model):
    # Fixed list of categories -> keeps data clean for the pie chart.
    # (A free-text category field would create messy duplicates like
    # "Food" vs "food" vs "Food " when grouping for the chart.)
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('travel', 'Travel'),
        ('shopping', 'Shopping'),
        ('bills', 'Bills'),
        ('entertainment', 'Entertainment'),
        ('health', 'Health'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    date = models.DateField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-created_at']  # newest expenses first

    def __str__(self):
        return f"{self.title} - Rs.{self.amount} ({self.user.username})"
