"""
==========================================================
SETTINGS.PY  -  Main configuration file for our Django project
==========================================================
Control panel of the whole project. Tells Django which apps are
installed, which database to use (MySQL), where templates/static
files live, and login/logout redirect behavior.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# -----------------------------------------------------
# SECURITY KEY
# -----------------------------------------------------
# Change this before deploying to production. Better: load from an
# environment variable instead of hardcoding it.
SECRET_KEY = 'django-insecure-change-this-before-deploying-xyz123'

DEBUG = True

ALLOWED_HOSTS = ['*']


# -----------------------------------------------------
# INSTALLED APPS
# -----------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Our own apps
    'accounts',   # signup / login / logout
    'expenses',   # add/edit/delete expenses + dashboard + chart
]


# -----------------------------------------------------
# MIDDLEWARE
# -----------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'expense_tracker.urls'


# -----------------------------------------------------
# TEMPLATES
# -----------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],   # our shared templates/ folder
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'expense_tracker.wsgi.application'


# -----------------------------------------------------
# DATABASE -> MySQL
# -----------------------------------------------------
# Create the DB first in MySQL shell:
#   CREATE DATABASE expense_tracker_db CHARACTER SET utf8mb4;
# Then fill in your real MySQL username/password below.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'expense_tracker_db',
        'USER': 'root',
        'PASSWORD': 'Agwinjino17',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}


# -----------------------------------------------------
# PASSWORD VALIDATION
# -----------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# -----------------------------------------------------
# INTERNATIONALIZATION
# -----------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True


# -----------------------------------------------------
# STATIC FILES (CSS, JS)
# -----------------------------------------------------
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# -----------------------------------------------------
# AUTH REDIRECTS
# -----------------------------------------------------
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_URL = 'login'
