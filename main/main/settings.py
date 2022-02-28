"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import whitenoise


import django_heroku


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#

# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = 'django-insecure-*)^=n&4@1&*e^qcmnf@hfkjl2b#-a-47&3%)@9-(537tj$1+rj'

DEBUG = False

ALLOWED_HOSTS = ['lightw.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # local apps
    'apps.pages',
    'apps.posts',
    'apps.blogs',
    'apps.polls',
    'apps.enrolnew',
    'apps.users',
    'apps.news',
    'apps.bookstore',
    'apps.orders',
    'apps.courses',

    # APIs
    'apps.booksapi',
    'apps.todoapi',
    'apps.blogapi',

    # 3rd party
    'crispy_forms',
    'rest_framework',
    'rest_framework.authtoken',  # token authentication
    'rest_framework_swagger',

    # 'rest_auth', # this app can override our custom user model for login/logout/reset password functionality
    # user registration app to ovveride default user app
    # 'allauth',
    # 'allauth.account',
    # 'allauth-socialaccount',
    # 'rest_auth',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    ‘whitenoise.middleware.WhiteNoiseMiddleware’,
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'main/templates')],
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

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        # 'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': 'postgres',
        # 'USER': 'postgres',
        # 'PASSWORD': 'postgres',
        # 'HOST': 'localhost',
        # 'PORT': 5432
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'main\\static'),
]
STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = 'pages:home'
LOGOUT_REDIRECT_URL = 'pages:home'
AUTH_USER_MODEL = 'users.CustomUser'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
SITE_ID = 1

# sendgrid settings
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = ""
EMAIL_PORT = 465
EMAIL_USE_TLS = True
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'main\\media')

#  add stripe
STRIPE_TEST_PUBLISHABLE_KEY = os.environ.get('enter key here')
STRIPE_TEST_SECRET_KEY = os.environ.get('enter key')

# rest_framework user access settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # allow any one permissions
        # 'rest_framework.permissions.AllowAny',
        # allow anyone to view or crud for authenticated users
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    # user authentication settings - session/token authentication
    # default available options are sessionauthentication and basicauthentication
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        # basic authentication can be override with tokenauthentication

        # 'rest_framework.authentication.BasicAuthentication',

        # token authentication
        'rest_framework.authentication.TokenAuthentication',
    ],
    # add following settings to enable api schemas
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',

}

django_heroku.settings(locals())
