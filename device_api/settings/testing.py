from django.core.management.utils import get_random_secret_key

from .base import *

SECRET_KEY = get_random_secret_key()

DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "device-api-test"}
}
