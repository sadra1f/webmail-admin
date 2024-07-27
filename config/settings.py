"""
Django settings for admin_panel project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-9)(dn6z*nd0_i#njt=z%i9d=*mn65&9+hl5*yfc6on0+ast-e4",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "False").lower() in ("true", "1")

ALLOWED_HOSTS = [
    item.strip() for item in os.environ.get("ALLOWED_HOSTS", "").split(",")
] + [
    "127.0.0.1",
    "localhost",
]

INTERNAL_IPS = [
    "127.0.0.1",
]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "revproxy",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "panel",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CSRF_COOKIE_SECURE = os.environ.get(
    "CSRF_COOKIE_SECURE",
    default="True",
).lower() in ("true", "1")
SESSION_COOKIE_SECURE = os.environ.get(
    "SESSION_COOKIE_SECURE",
    default="True",
).lower() in ("true", "1")

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASE_NAME = os.environ.get("DB_NAME", "webmail_admin")
# DATABASE_UNAME = os.environ.get("DB_UNAME", "root")
# DATABASE_PASSWORD = os.environ.get("DB_PASS", "")
# DATABASE_HOST = os.environ.get("DB_HOST", "127.0.0.1")
# DATABASE_PORT = os.environ.get("DB_PORT", "3306")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    # "default": {
    #     "ENGINE": "django.db.backends.mysql",
    #     "NAME": DATABASE_NAME,
    #     "USER": DATABASE_UNAME,
    #     "PASSWORD": DATABASE_PASSWORD,
    #     "HOST": DATABASE_HOST,
    #     "PORT": DATABASE_PORT,
    #     "OPTIONS": {
    #         "init_command": "SET default_storage_engine=INNODB",
    #         "sql_mode": "STRICT_TRANS_TABLES",
    #     },
    # }
}

CACHE_TABLE_CULLING_QUERY = (
    "DELETE FROM cache_table WHERE expires < CONVERT_TZ(now(),'+04:30','+00:00')"
)


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Logging
# https://docs.djangoproject.com/en/5.0/topics/logging/

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[{levelname}][{asctime}][{module}]\n{message}\n",
            "style": "{",
        }
    },
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "filename": "log.log",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "": {
            "handlers": ["file"],
        },
    },
}


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Sites framework
# https://docs.djangoproject.com/en/5.0/ref/contrib/sites/

SITE_ID = 1


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static_production"
STATICFILES_DIRS = [BASE_DIR / "static"]

# MEDIA_URL = "/media/"
# MEDIA_ROOT = (
#     BASE_DIR / "media"
#     if DEBUG
#     else os.environ.get("MEDIA_ROOT", "/home/app/public_html/media")
# )


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Roundcube configurations

ROUNDCUBE_ENABLE = os.environ.get("ROUNDCUBE_ENABLE", "False").lower() in ("true", "1")
ROUNDCUBE_URL = os.environ.get("ROUNDCUBE_URL")
ROUNDCUBE_LOGIN_URL = os.environ.get("ROUNDCUBE_LOGIN_URL", "/roundcube/?_autologin=1")

# Mailserver configurations
POSTFIX_SSH_ROOT_PASSWORD = os.environ.get("POSTFIX_SSH_ROOT_PASSWORD")
