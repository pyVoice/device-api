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
	'default': {
		'ENGINE': 'djongo',
        'NAME': 'pyvoice-device-api',
        'CLIENT': {
            'host': '127.0.0.1',
        }
	},
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
]

REST_FRAMEWORK = {
    'PAGE_SIZE': 200,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    #'DATETIME_FORMAT': '%s000',
}