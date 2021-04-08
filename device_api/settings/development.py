import socket

import environ

from .base import *

env = environ.Env()
environ.Env.read_env()

DEBUG = True

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = []

DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "db.sqlite"},
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
]

REST_FRAMEWORK = {
    "PAGE_SIZE": 200,
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    # 'DATETIME_FORMAT': '%s000',
}
