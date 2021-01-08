import environ


env = environ.Env(
	ALLOWED_HOSTS=(list, []),
)

DEBUG = env('DEBUG')

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env('ALLOWED_HOSTS')

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': env('MONGODB_DB_NAME'),
        'CLIENT': {
            'host': env('MONGODB_DB_HOST'),
            'port': env('MONGODB_DB_PORT'),
            'username': env('MONGODB_DB_USERNAME'),
            'password': env('MONGODB_DB_PASSWORD'),
        }
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK += {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}