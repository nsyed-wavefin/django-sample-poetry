"""
Django settings with Poetry.

Generated by 'django-admin startproject'.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import environ, os

ROOT_DIR = environ.Path(__file__) - 4  # (project_name/config/settings/base.py - 3 = project_name/)
CONFIG_DIR = ROOT_DIR.path('config')
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# PROJECT_ROOT = os.path.dirname(BASE_DIR)

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

os.environ["DJANGO_ALLOWED_HOSTS"]

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

SITE_ID = 1

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True
