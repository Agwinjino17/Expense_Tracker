"""
==========================================================
URLS.PY (project level)
==========================================================
Main URL router. Delegates to each app's own urls.py.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('expenses.urls')),   # dashboard + expense CRUD live at root
]
