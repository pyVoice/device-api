from .base import *
import environ


environ.Env.read_env(
	ALLOWED_HOSTS=(list, []),
)

DEBUG = True

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env('ALLOWED_HOSTS')

DATABASES = {
	'default': {
		'ENGINE': 'djongo',
        'NAME': 'pyvoice-device-api',
        'CLIENT': {
            'host': '127.0.0.1',
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