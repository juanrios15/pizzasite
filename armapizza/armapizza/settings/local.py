from .base import *
from django.core.exceptions import ImproperlyConfigured
import json

with open("secret.json") as f:
    secret = json.loads(f.read())

def get_secret(secret_name,secrets = secret):
    try:
        return secrets[secret_name]
    except:
        msg= "La variable %s no existe" % secret_name
        raise ImproperlyConfigured(msg)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret("SECRET_KEY")

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / get_secret("DB_NAME"),
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
