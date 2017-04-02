from .common import *
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#=3v0_a%@qz4m^gukz^epe(a)apfch3bkb0mmw=-!8-chxoa^$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.environ['SPIN_DB_NAME'],
        'USER': os.environ['SPIN_DB_USER'],
        'PASSWORD': os.environ['SPIN_DB_PWD'],
        'HOST': os.environ['SPIN_DB_HOST'],
        'PORT': os.environ['SPIN_DB_PORT'],
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'info@spinthewheel.gr'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
EMAIL_PORT = 1025
