from .base import *
import os

THIRD_PARTY_APPS= ["debug_toolbar",]

INSTALLED_APPS+= THIRD_PARTY_APPS

THIRD_PARTY_MIDDLEWARE=["debug_toolbar.middleware.DebugToolbarMiddleware",]

MIDDLEWARE+= THIRD_PARTY_MIDDLEWARE

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG")


INTERNAL_IPS = [
    "127.0.0.1",
]