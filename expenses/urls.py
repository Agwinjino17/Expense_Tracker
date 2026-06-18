"""
==========================================================
URLS.PY (expenses app)
==========================================================
Maps URL paths to view functions for everything expense-related.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('expenses/', views.expense_list_view, name='expense_list'),
    path('expenses/add/', views.add_expense_view, name='add_expense'),
    path('expenses/<int:pk>/edit/', views.edit_expense_view, name='edit_expense'),
    path('expenses/<int:pk>/delete/', views.delete_expense_view, name='delete_expense'),
    path('api/chart-data/', views.chart_data_view, name='chart_data'),
]
