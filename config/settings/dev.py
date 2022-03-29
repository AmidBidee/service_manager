"""
development settings for service manager
DONT USE THIS FOR PRODUCTION OR ON PREMESISES
"""
from config.settings.base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': getenv('DB_NAME'),
        'USER': getenv('DB_USER'),
        'HOST': getenv('DB_HOST'),
        'PORT': getenv('DB_PORT'),
        'PASSWORD': getenv('USER_PASSWORD')
    }
}