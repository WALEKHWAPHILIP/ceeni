import os
from pathlib import Path

# -----------------------------------------------------------------------------
# BASE DIRECTORY
# -----------------------------------------------------------------------------
# BASE_DIR points to the root of the project directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# -----------------------------------------------------------------------------
# SECURITY
# -----------------------------------------------------------------------------
# Secret key should never be hardcoded in production.
# Using environment variable with a fallback insecure key for dev/testing only.
SECRET_KEY = os.getenv("SECRET_KEY", "dummy-insecure-key")

# -----------------------------------------------------------------------------
# APPLICATIONS
# -----------------------------------------------------------------------------
# Core Django apps included in most projects.
INSTALLED_APPS = [
    "django.contrib.admin",           # Admin interface
    "django.contrib.auth",            # Authentication framework
    "django.contrib.contenttypes",    # Content type system (permissions)
    "django.contrib.sessions",        # Session framework
    "django.contrib.messages",        # Messaging framework (flash messages)
    "django.contrib.staticfiles",     # Static file management
]

# -----------------------------------------------------------------------------
# MIDDLEWARE
# -----------------------------------------------------------------------------
# Middleware layers process requests/responses globally.
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",             # Security enhancements
    "django.contrib.sessions.middleware.SessionMiddleware",      # Manages sessions across requests
    "django.middleware.common.CommonMiddleware",                 # Adds common headers and options
    "django.middleware.csrf.CsrfViewMiddleware",                 # Protects against CSRF attacks
    "django.contrib.auth.middleware.AuthenticationMiddleware",   # Associates users with requests
    "django.contrib.messages.middleware.MessageMiddleware",      # Enables messaging framework
    "django.middleware.clickjacking.XFrameOptionsMiddleware",    # Prevents clickjacking
]

# -----------------------------------------------------------------------------
# URL AND WSGI CONFIGURATION
# -----------------------------------------------------------------------------
ROOT_URLCONF = "config.urls"              # Root URL dispatcher module
WSGI_APPLICATION = "config.wsgi.application"  # WSGI application callable for servers

# -----------------------------------------------------------------------------
# INTERNATIONALIZATION AND TIMEZONE
# -----------------------------------------------------------------------------
LANGUAGE_CODE = "en-us"                   # Language code (en-us = English US)
TIME_ZONE = "Africa/Nairobi"               # Project time zone (Kenya's time zone)
USE_I18N = True                           # Enable Django’s translation system
USE_TZ = True                             # Enable timezone-aware datetimes

# -----------------------------------------------------------------------------
# STATIC FILES (CSS, JavaScript, Images)
# -----------------------------------------------------------------------------
STATIC_URL = "/static/"                    # URL prefix for static files (CSS, JS, images)

# -----------------------------------------------------------------------------
# DEFAULT PRIMARY KEY FIELD TYPE
# -----------------------------------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"  # Default for model primary keys








# -------------------------------------------------------------------------
# TEMPLATES CONFIGURATION
# -------------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",  # Required for admin
        "DIRS": [],  # Add custom template directories here, if needed
        "APP_DIRS": True,  # Enables loading templates from installed apps (like admin)
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",  # Mandatory for admin
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]







# -----------------------------------------------------------------------------
# NOTES:
# - Add environment-specific settings (dev, prod) by extending this base.py in
#   separate files (e.g., dev.py, prod.py) to keep settings modular and secure.
# - Consider using python-decouple or django-environ for better env var management.
# - For production, ensure SECRET_KEY and other sensitive data are stored securely.
# - Further customize INSTALLED_APPS and MIDDLEWARE as your project grows.


