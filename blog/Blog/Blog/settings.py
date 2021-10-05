"""
Django settings for Blog project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

from django.urls.conf import path

#from Blog.local_settings import 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # API framework
    'rest_framework',
    'rest_framework.authtoken',
    # apps criados
    'main.apps.MainConfig',
    'usuarios.apps.UsuariosConfig',
    'social.apps.SocialConfig',
    'comentarios.apps.ComentariosConfig',
    # Bibliotecas auxiliares
    'ckeditor',
    'ckeditor_uploader',
    'crispy_forms',
    'localflavor',
    'social_django',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

## ATENÇÃO! 
# Esta configuração foi migrada para o local_settings.py 
#
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.Email.Backend'
EMAIL_HOST = 'smtp.gmail.com:587'
#EMIAL_PORT = 587      
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'equipeinfocode@gmail.com'
EMAIL_HOST_PASSWORD = 'Equipeinfocode1234'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = 'main/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = 'static'

MEDIA_URL = '/static/'

# Bootstrap Form

CRISPY_TEMPLATE_PACK = 'bootstrap4'

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ]
}

# Redirecionamento de login e logout

LOGIN_REDIRECT_URL = "/social/feed"
LOGOUT_REDIRECT_URL = "/accounts/login"

# Biblioteca

CKEDITOR_UPLOAD_PATH = 'uploades/'

# Local_settings

with open("Blog/local_settings.py") as infile:
    exec(infile.read())

    AUTHENTICATION_BACKENDS = [
        'social_core.backends.google.GoogleOAuth2',
        'django.contrib.auth.backends.ModelBackend',
        'social_core.backends.facebook.FacebookOAuth2',
    ]



SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '816267412622-anmgofhh5et3gbgfr1j7bvfpjgtjcm46.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'oKyUtF10kS75h4KEoLszdzK4'


SOCIAL_AUTH_FACEBOOK_KEY = '303515681619009'
SOCIAL_AUTH_FACEBOOK_SECRET = '918d9bdab99da8ee60535fbe03b0e7d8'