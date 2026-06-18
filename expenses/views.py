"""
==========================================================
VIEWS.PY (expenses app)
==========================================================
Each function here handles one URL. @login_required makes sure
only logged-in users can reach these pages, and every queryset
is filtered by `user=request.user` so people only ever see and
edit THEIR OWN expenses (not anyone else's).
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Sum
from django.utils import timezone

from .models import Expense
from .forms import ExpenseForm


@login_required
def dashboard_view(request):
    """Main page: shows recent expenses, total spent, and the pie chart."""
    expenses = Expense.objects.filter(user=request.user)

    total_spent = expenses.aggregate(total=Sum('amount'))['total'] or 0

    # This month's total (for the summary card)
    today = timezone.now().date()
    this_month_total = expenses.filter(
        date__year=today.year, date__month=today.month
    ).aggregate(total=Sum('amount'))['total'] or 0

    # Group totals by category -> this feeds the pie chart via JS
    category_totals = (
        expenses.values('category')
        .annotate(total=Sum('amount'))
        .order_by('-total')
    )

    context = {
        'expenses': expenses[:8],          # show only the latest 8 on dashboard
        'total_spent': total_spent,
        'this_month_total': this_month_total,
        'category_totals': list(category_totals),
        'expense_count': expenses.count(),
    }
    return render(request, 'expenses/dashboard.html', context)


@login_required
def expense_list_view(request):
    """Full list of every expense the user has, with category filter."""
    expenses = Expense.objects.filter(user=request.user)

    selected_category = request.GET.get('category', '')
    if selected_category:
        expenses = expenses.filter(category=selected_category)

    context = {
        'expenses': expenses,
        'categories': Expense.CATEGORY_CHOICES,
        'selected_category': selected_category,
    }
    return render(request, 'expenses/expense_list.html', context)


@login_required
def add_expense_view(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user   # attach to the logged-in user
            expense.save()
            messages.success(request, 'Expense added.')
            return redirect('dashboard')
    else:
        form = ExpenseForm(initial={'date': timezone.now().date()})

    return render(request, 'expenses/expense_form.html', {'form': form, 'mode': 'Add'})


@login_required
def edit_expense_view(request, pk):
    # get_object_or_404 + user=request.user together stop one user from
    # editing another user's expense just by guessing a different pk in the URL.
    expense = get_object_or_404(Expense, pk=pk, user=request.user)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, 'Expense updated.')
            return redirect('dashboard')
    else:
        form = ExpenseForm(instance=expense)

    return render(request, 'expenses/expense_form.html', {'form': form, 'mode': 'Edit'})


@login_required
def delete_expense_view(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == 'POST':
        expense.delete()
        messages.success(request, 'Expense deleted.')
        return redirect('dashboard')
    return render(request, 'expenses/expense_confirm_delete.html', {'expense': expense})


@login_required
def chart_data_view(request):
    """
    Returns category totals as JSON. The dashboard page calls this
    with fetch() and draws the pie chart with Chart.js -> this is
    the 'full stack' piece: JS talking to a Django JSON endpoint.
    """
    expenses = Expense.objects.filter(user=request.user)
    category_totals = (
        expenses.values('category')
        .annotate(total=Sum('amount'))
        .order_by('-total')
    )

    category_labels = dict(Expense.CATEGORY_CHOICES)
    data = {
        'labels': [category_labels.get(item['category'], item['category']) for item in category_totals],
        'totals': [float(item['total']) for item in category_totals],
    }
    return JsonResponse(data)
