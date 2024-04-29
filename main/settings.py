"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from pathlib import Path
import pytesseract

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PATH_URL = 'visyonOCR'
WINDOWS = True
SEPARADOR = '\\' if WINDOWS == True else '/'
##Exibir imagens durante o processamento - MODO DEBUG
EXIBIR_IMAGENS_MD = False
STATIC_URL = 'static'+'/'

#CNN CONFIGURATION
CNN_MIN_PREDICTION = 0.70

#OCR TESSERACT
#pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"
pytesseract.pytesseract.tesseract_cmd ="C:\Program Files\Tesseract-OCR\\tesseract.exe"
TESSERACT_LANGUAGE = 'eng'

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = False

#CNN YOLO
DATASET_YOLO_CFG_PATH = str(BASE_DIR)+SEPARADOR+'conf'+SEPARADOR+'yolo_dataset'+SEPARADOR+'cfg'
DATASET_YOLO_OBJ_PATH = str(BASE_DIR)+SEPARADOR+'conf'+SEPARADOR+'yolo_dataset'+SEPARADOR+'data'+SEPARADOR+'obj'
DATASET_YOLO_VALID_PATH = str(BASE_DIR)+SEPARADOR+'conf'+SEPARADOR+'yolo_dataset'+SEPARADOR+'data'+SEPARADOR+'valid'
DATASET_YOLO_DATA_PATH = str(BASE_DIR)+SEPARADOR+'conf'+SEPARADOR+'yolo_dataset'+SEPARADOR+'data'
DATASET_YOLO_CNN_PATH = str(BASE_DIR)+SEPARADOR+'conf'+SEPARADOR+'yolo_dataset'+SEPARADOR+'cnn'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+4l26o^=7b$x=jsi*z3l-e$tugd^yse#fumfcf*_-#@1190m_s'

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
    'rest_framework_swagger',
    'rest_framework',
    'drf_spectacular',
    'core',
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

ROOT_URLCONF = 'main.urls'

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

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    # YOUR SETTINGS
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'visyonOCR',
    'DESCRIPTION': 'Sistema que usa processamento de imagens, CNN YOLO e OCR para extração textual em imagens',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/



# Python Code
# project/project/settings.py

# Celery settings
CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"

