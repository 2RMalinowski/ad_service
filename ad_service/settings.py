from auth import secret_key, pg_pass
<<<<<<< HEAD
import dj_database_url
import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMP_DIR = os.path.join(BASE_DIR, 'templates')
=======
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
>>>>>>> 2a4ab3107b197b6efa4489ff41b7551b7f6cc485


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

<<<<<<< HEAD
ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']
=======
ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']
>>>>>>> 2a4ab3107b197b6efa4489ff41b7551b7f6cc485


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ui_app',
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

<<<<<<< HEAD
ROOT_URLCONF = 'ad_service.urls'
=======
ROOT_URLCONF = 'ui_app.urls'
>>>>>>> 2a4ab3107b197b6efa4489ff41b7551b7f6cc485

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
<<<<<<< HEAD
        'TEMP_DIR'
=======
>>>>>>> 2a4ab3107b197b6efa4489ff41b7551b7f6cc485
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

<<<<<<< HEAD
WSGI_APPLICATION = 'ad_service.wsgi.application'
    
=======
WSGI_APPLICATION = 'ui_app.wsgi.application'

>>>>>>> 2a4ab3107b197b6efa4489ff41b7551b7f6cc485

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
<<<<<<< HEAD
        'NAME': 'ad_service',
=======
        'NAME': 'ui_app',
>>>>>>> 2a4ab3107b197b6efa4489ff41b7551b7f6cc485
        'USER': 'postgres',
        'PASSWORD': pg_pass,
        'HOST': '127.0.0.1',
        'PORT': 5432
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
<<<<<<< HEAD
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
=======
>>>>>>> 2a4ab3107b197b6efa4489ff41b7551b7f6cc485
