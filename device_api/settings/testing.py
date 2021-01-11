from .base import *
from django.core.management.utils import get_random_secret_key


SECRET_KEY = get_random_secret_key()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'device-api-test'
    }
}

TEST_RUNNEER = ['django_nose.NoseTestSuiteRunner']

NOSE_ARGS = ['--with-spec', '--spec-color']
