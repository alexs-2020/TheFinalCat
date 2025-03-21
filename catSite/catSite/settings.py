"""
Django settings for catSite project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
import dotenv
from pathlib import Path

from socials.apps import SocialConfig


import dj_database_url

dotenv.load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-fy8t5!u^jr#2&9eekoet#4n+_p6u6b$qdry5tbc0omeicdnt6j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['www.britishmerlinblue.com', 'thefinalcat-production.up.railway.app', 'localhost','127.0.0.1', 'healthcheck.railway.app', 'catadoptionsite-production.up.railway.app']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'




# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "whitenoise.runserver_nostatic",  # Ensure Whitenoise serves static files
    'core',
    'catList',
    'contact',
    # 'socials.apps.SocialConfig',
    'image_cropping',
    'easy_thumbnails',
]

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Must be before other middlewares
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # ✅ CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CSRF_TRUSTED_ORIGINS = ['http://localhost:8000', 'https://www.britishmerlinblue.com',  "https://thefinalcat-production.up.railway.app"]
CSRF_COOKIE_HTTPONLY = False  # ✅ Allows JavaScript to read CSRF cookies
CSRF_COOKIE_SECURE = False    # ❌ Set to True only if using HTTPS
CSRF_COOKIE_SAMESITE = 'Lax'  # ✅ Allows CSRF cookies to be sent correctly

ROOT_URLCONF = 'catSite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'catSite.wsgi.application'

# settings.py
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',  # Required for image cropping
) + ('easy_thumbnails.processors.colorspace', 'easy_thumbnails.processors.autocrop', 'easy_thumbnails.processors.scale_and_crop', 'easy_thumbnails.processors.filters')


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

deployed = True

if deployed:

    DATABASES = {
        'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': dj_database_url.config(default=os.getenv('LOCAL_DATABASE_URL'))
    }


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

from django.utils.translation import gettext_lazy as _

# Set up default language
LANGUAGE_CODE = 'en'

# Enable localization
USE_I18N = True
USE_L10N = True

# Define supported languages
LANGUAGES = [
    ('en', _('English')),
    ('es', _('Spanish')),
]

# Path for translation files
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Static files
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")  # New location for production

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # SMTP server for Gmail
EMAIL_PORT = 587  # TLS port for Gmail
EMAIL_USE_TLS = True  # Enable TLS
EMAIL_HOST_USER = 'your_email@gmail.com'  # Your email address
EMAIL_HOST_PASSWORD = 'your_app_specific_password'  # App-specific password for Gmail

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
