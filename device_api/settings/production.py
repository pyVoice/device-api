import os

import dj_database_url
import environ
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env(
    ALLOWED_HOSTS=(list, []),
)

DEBUG = env("DEBUG")

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env("ALLOWED_HOSTS")

DATABASES = {"default": dj_database_url.config(conn_max_age=500)}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

REST_FRAMEWORK = {
    "PAGE_SIZE": 25,
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
}

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/assets/"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

sentry_sdk.init(
    dsn="https://88ae5f772ae945889d5fa9f93ed9cdbf@o520978.ingest.sentry.io/5665502",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
)
