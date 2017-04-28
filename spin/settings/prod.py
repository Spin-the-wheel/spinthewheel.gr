from .common import *
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRETS.get('secret_key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
        "spinthewheel.gr"
        ] + SECRETS.get('allowed_hosts', [])

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': SECRETS.get('db_name'),
        'USER': SECRETS.get('db_user'),
        'PASSWORD': SECRETS.get('db_password'),
        'HOST': SECRETS.get('db_host'),
        'PORT': SECRETS.get('db_port'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = SECRETS.get('email_from')
EMAIL_HOST = SECRETS.get('e_host')
EMAIL_HOST_USER = SECRETS.get('e_host_user')
EMAIL_HOST_PASSWORD = SECRETS.get('e_host_password')
EMAIL_USE_TLS = SECRETS.get('e_tls')
EMAIL_PORT = SECRETS.get('e_port')
