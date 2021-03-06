"""
Django settings for buskr project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ilp2))8xzc(fm@zp^99d@mmewrq9x*_+-ok9s-ir)&#h-!--w+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'buskr', 'templates'),
)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'artist',
    'donor',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'buskr.urls'

WSGI_APPLICATION = 'buskr.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'data', 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

DEFAULT_PAYPAL_CLIENT_ID = 'EOJ2S-Z6OoN_le_KS1d75wsZ6y0SFdVsY9183IvxFyZp'
DEFAULT_PAYPAL_SECRET = 'EClusMEUk8e9ihI7ZdVLF5cZ6y0SFdVsY9183IvxFyZp'
DEFAULT_PAYPAL_MODE = 'sandbox'
PAYPAL_CLIENT_ID = os.environ.get(
    'PAYPAL_CLIENT_ID',
    DEFAULT_PAYPAL_CLIENT_ID)
PAYPAL_SECRET = os.environ.get(
    'PAYPAL_SECRET',
    DEFAULT_PAYPAL_SECRET)
PAYPAL_MODE = os.environ.get(
    'PAYPAL_MODE',
    DEFAULT_PAYPAL_MODE)
