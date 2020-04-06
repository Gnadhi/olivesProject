"""
Django settings for olivesProject project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.template.backends import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Builds a path to the templates folder
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

# Builds a path to the static folder
STATIC_DIR = os.path.join(BASE_DIR, "static")

# Builds a path to the static folder
MEDIA_DIR = os.path.join(BASE_DIR, "media")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3kju1w^h09g39hu!oba*_dsf4^v469^7=@p%mu78h!7p=9yqlr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = []

# Variables to be used throughout django.


# ------------ These variables are for user authentication. ----------#

# If True users can register.
REGISTRATION_OPEN = True

# If  True, users will be automatically logged in after registering.
REGISTRATION_AUTO_LOGIN = True

# The Url Django redirects the user to after logging in.
LOGIN_REDIRECT_URL = 'olives:index'

# The page users are directed to if they are not logged in.The registration package uses this, too. 
LOGIN_URL = 'auth_login'

# As we are using a custom user model we need to add this.
# AUTH_USER_MODEL = 'olives.User'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'olives',
    'registration',
]

ROOT_URLCONF = 'olivesProject.urls'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [TEMPLATE_DIR],
        'DIRS': [os.path.join(BASE_DIR, 'template/registration'), TEMPLATE_DIR],
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

WSGI_APPLICATION = 'olivesProject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

# Use Argon2Password Hasher as it provides more security.
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images, bootstrap)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [STATIC_DIR, ]

# Media Files

MEDIA_ROOT = MEDIA_DIR

MEDIA_URL = "/media/"

# Email Settings
# Using a Gmail account called olivesandpesto1234@gmail.com to send the emails through  
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "olivesandpesto1234@gmail.com"
EMAIL_HOST_PASSWORD = "ilovemaths1234"
