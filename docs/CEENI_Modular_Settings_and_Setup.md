
# 🛠️ CEENI Django Project Setup — Full Technical Documentation (Phase 1 + Modular Settings)

This document captures the complete technical setup of the CEENI platform up to admin access — including all steps, decisions, fixes, and structured modular settings implementation.

---

## ✅ Substep: Create the Django Project and Modular Settings Structure

This section lays the foundation of the Django backend using a modular settings system.

---

### 🧱 Step 1: Create Django Project

Inside `C:\apps\ceeni`, run:

```bash
django-admin startproject config .
```

✅ This creates:

```
ceeni/
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py  ← Will be renamed
│   ├── urls.py
│   └── wsgi.py
├── manage.py
```

---

### ⚙️ Step 2: Create Modular Settings Structure

Inside `config/`:

```bash
mkdir config\settings
move config\settings.py config\settings\base.py
```

Create these files inside `config/settings/`:

```python
# __init__.py
import os
env = os.getenv("DJANGO_ENV", "dev")
if env == "prod":
    from .prod import *
else:
    from .dev import *
```

```python
# dev.py
from .base import *
from dotenv import load_dotenv
load_dotenv()

DEBUG = True
ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

```python
# prod.py
from .base import *

DEBUG = False
ALLOWED_HOSTS = ["ceeni.walsoftai.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}
```

---

### 🔁 Step 3: Create `.env` and `.env.example`

At root:

```bash
copy NUL .env
copy .env .env.example
```

`.env`:
```env
DJANGO_ENV=dev
SECRET_KEY=ij#7_m41v89*do@_$!()*+@mlsi%7r-&t%7oo0dg%e6ic$7+o1
DB_NAME=ceeni_db
DB_USER=ceeni_user
DB_PASSWORD=@0BusiaKenya
DB_HOST=localhost
DB_PORT=5432
```

`.env.example`:
```env
DJANGO_ENV=dev
SECRET_KEY=your-secret-key-here
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

---

## 🐘 PostgreSQL Installation and Setup

- Version: PostgreSQL 17.5
- Installation Path: `C:\Program Files\PostgreSQL\17\bin`
- CLI Tool: `psql` added to system PATH

### Create User and DB

```sql
psql -U postgres

CREATE USER ceeni_user WITH PASSWORD '@0BusiaKenya';
CREATE DATABASE ceeni_db;
GRANT ALL PRIVILEGES ON DATABASE ceeni_db TO ceeni_user;
```

### Fix Schema Permissions (Required)

```sql
\c ceeni_db
ALTER SCHEMA public OWNER TO ceeni_user;
\dn+
```

---

## ⚙️ base.py Configuration (with TEMPLATES)

```python
# TEMPLATES CONFIGURATION
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

---

## 🔄 Run Migrations

```bash
python manage.py migrate
```

✅ Success confirmed after schema ownership fix.

---

## 🔐 Django Admin Superuser

```bash
python manage.py createsuperuser
```

Inputs:

- Username/Email: `sales@walsoftcomputers.com`
- Password: `@0BusiaKenya`

---

## ✅ You Are Now Ready for App Development

Next steps:
- Create Django apps: `bill`, `views_submission`, `analytics`, etc.
- Register apps in `INSTALLED_APPS`
- Start frontend design with Tailwind + HTMX

