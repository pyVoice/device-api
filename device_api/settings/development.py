from .base import *
import environ

env = environ.Env(
    DEBUG=(bool, True),
)

environ.Env.read_env()

DEBUG = env('DEBUG')

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = []

DATABASES = {
	# 'default': {
	# 	'ENGINE': 'djongo',
 #        'NAME': 'pyvoice-device-api',
 #        'CLIENT': {
 #            'host': '127.0.0.1',
 #        }
	# },
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'pyvoice-device-dev',
        'CLIENT': {
            'host': '***REMOVED***',
        }
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
]

REST_FRAMEWORK = {
    'PAGE_SIZE': 25,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
}