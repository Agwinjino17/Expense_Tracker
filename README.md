# Ledger — Personal Expense Tracker (Django + MySQL)

A multi-user expense tracker. Each person signs up, logs in, and sees
only their own expenses. Built with your exact stack: HTML, CSS,
JavaScript, Python, Django, MySQL.

---

## What's inside

```
expense_tracker/
├── manage.py
├── requirements.txt
├── expense_tracker/    -> project settings, main urls.py
├── accounts/           -> signup / login / logout
├── expenses/           -> add/edit/delete expenses, dashboard, chart API
├── templates/          -> all HTML files
└── static/css, static/js -> styling + dashboard chart script
```

## How it works

- **accounts app**: signup creates a user and logs them in immediately.
  Login/logout reuse Django's own built-in views — no need to write
  password-checking logic yourself, Django handles hashing & sessions.
- **expenses app**: every `Expense` row has a `user` foreign key. Every
  view filters `Expense.objects.filter(user=request.user)`, so one
  user can never see or edit another user's data — even if they guess
  a different ID in the URL (tested: returns 404).
- **Dashboard chart**: the page calls `/api/chart-data/` with
  JavaScript `fetch()`, which returns JSON (category totals), and
  Chart.js draws a doughnut chart from it. This is the "full stack"
  piece — JS talking to a Django JSON endpoint, not just a server
  rendered page.

## Setup steps

### 1. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

> Note: `mysqlclient` sometimes needs MySQL dev headers installed first.
> On Windows, installing "MySQL Connector C" or a prebuilt wheel usually
> fixes install errors. On Ubuntu: `sudo apt install default-libmysqlclient-dev`

### 3. Create the MySQL database
```sql
CREATE DATABASE expense_tracker_db CHARACTER SET utf8mb4;
```

### 4. Update database credentials
Open `expense_tracker/settings.py` → `DATABASES` and confirm your
MySQL username/password are correct (defaults to `root` / your password).

### 5. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. (Optional) Create an admin account
```bash
python manage.py createsuperuser
```
Lets you view/manage all expenses across all users at `/admin/`.

### 7. Run the server
```bash
python manage.py runserver
```
Visit: http://127.0.0.1:8000/ → you'll be redirected to sign up / log in.

## Pages you get

| URL                          | What it shows                              |
|-------------------------------|---------------------------------------------|
| `/accounts/signup/`           | Create an account                          |
| `/accounts/login/`            | Sign in                                    |
| `/`                            | Dashboard — totals, recent entries, chart  |
| `/expenses/`                   | Full list of entries, filterable by category |
| `/expenses/add/`               | Add a new expense                          |
| `/expenses/<id>/edit/`         | Edit an expense                            |
| `/expenses/<id>/delete/`       | Delete (with confirmation)                 |
| `/api/chart-data/`             | JSON — category totals for the logged-in user |
| `/admin/`                      | Django's built-in admin panel              |

## Why this project is good for your resume

- Real multi-user app with proper data isolation (not just CRUD on one
  shared table) — tested that User A cannot access User B's data.
- Django's built-in auth system used correctly (signup + session login).
- MySQL as the production-style database.
- JS `fetch()` calling a Django JSON endpoint to render a Chart.js
  chart — shows you can connect frontend and backend, not just
  template rendering.
- Clean, commented code — easy to explain line by line in interviews.

## Talking points for interviews

- "Why a ForeignKey to User instead of a separate table per user?" —
  one `Expense` table, filtered by `user=request.user` on every query;
  simpler and scales better than per-user tables.
- "How do you stop User A from editing User B's expense?" —
  `get_object_or_404(Expense, pk=pk, user=request.user)` — if the
  expense doesn't belong to that user, Django returns 404 instead of
  leaking that the row exists.
- "Why a JSON endpoint instead of just rendering the chart server-side?" —
  keeps the chart interactive/reusable on the client, and demonstrates
  a clean separation between data (Django) and presentation (JS/Chart.js).
