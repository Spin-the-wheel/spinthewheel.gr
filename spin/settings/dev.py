import json
from .common import *
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#=3v0_a%@qz4m^gukz^epe(a)apfch3bkb0mmw=-!8-chxoa^$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR.joinpath('db.sqlite3')),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'testing@example.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
EMAIL_PORT = 1025

BLOG = 'spinthewheel-en.tumblr.com'
