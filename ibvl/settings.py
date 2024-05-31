"""
Django settings for variome project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/

Quick-start development settings - unsuitable for production
See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/
"""

import os
import dotenv
from pathlib import Path
import dj_database_url

dotenv.load_dotenv()


IS_DEVELOPMENT = os.environ.get("ENVIRONMENT") != "production"
DOMAIN = os.environ.get("HOST") or "127.0.0.1"
print("domain is", DOMAIN)
DB = os.environ.get("DB") or "postgresql://variome:variome@localhost:5432/variome"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = (
    os.environ.get("DJANGO_SECRET_KEY")
    or "django-insecure-t=e420f^zm70rl(y%%wl6g!k97-od*b$i=y%qrq*z^r)_r-mc@"
)

AUTH_SERVER = os.environ.get("AUTH_SERVER", False)
AUTH_CLIENT_ID = os.environ.get("AUTH_CLIENT_ID", False)
AUTH_CLIENT_SECRET = os.environ.get("AUTH_CLIENT_SECRET", False)
AUTH_RELYING_PARTY_ID = os.environ.get("AUTH_RELYING_PARTY_ID", False)
AUTH_AUDIENCE = os.environ.get("AUTH_AUDIENCE", False)
AUTH_CA_BUNDLE = os.environ.get("AUTH_CA_BUNDLE", False)

IS_DEVELOPMENT = os.environ.get("ENVIRONMENT") != "production"

LANGUAGE_CODE = "en-us"
TIME_ZONE = os.environ.get("TZ") or "America/Vancouver"
USE_I18N = True
USE_TZ = True

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = IS_DEVELOPMENT

ALLOWED_HOSTS = ["127.0.0.1", "localhost", DOMAIN]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "django_extensions",
    "corsheaders",
    "tracking",
    "ibvl",
    "ibvl.library",
    "ibvl.library_access",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "tracking.middleware.VisitorTrackingMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
AUTHENTICATION_BACKENDS = []

if IS_DEVELOPMENT:
    AUTHENTICATION_BACKENDS = AUTHENTICATION_BACKENDS + [
        'django.contrib.auth.backends.ModelBackend'
    ]
    
if not IS_DEVELOPMENT or os.getenv("AUTH_AZUREAD", False):
    INSTALLED_APPS.append("django_auth_adfs")
#    MIDDLEWARE.append("django_auth_adfs.middleware.LoginRequiredMiddleware")
    AUTHENTICATION_BACKENDS = AUTHENTICATION_BACKENDS + [
        'django_auth_adfs.backend.AdfsAuthCodeBackend',
    ]

    AUTH_ADFS = {
        "SERVER": AUTH_SERVER,
        "CLIENT_ID": AUTH_CLIENT_ID,
        "GROUP_TO_FLAG_MAPPING": {
            "is_staff": ["admingroup", "superusergroup"],
            "is_superuser": "superusergroup",
        },
    }
    if AUTH_RELYING_PARTY_ID:
        AUTH_ADFS["RELYING_PARTY_ID"] = AUTH_RELYING_PARTY_ID
    if AUTH_AUDIENCE:
        AUTH_ADFS["AUDIENCE"] = AUTH_AUDIENCE
    if AUTH_CA_BUNDLE:
        AUTH_ADFS["CA_BUNDLE"] = AUTH_CA_BUNDLE
    
    CUSTOM_FAILED_RESPONSE_VIEW = 'ibvl.library_access.views.login_failed'
    
TRACK_AJAX_REQUESTS = True
TRACK_PAGEVIEWS = True
TRACK_ANONYMOUS_USERS = False
TRACK_IGNORE_URLS = [
    "^(?!api\/variant\/).*$"
]  # ignore everything other than api/variant
TRACK_IGNORE_STATUS_CODES = [400, 404, 403, 405, 410, 429, 500]

ROOT_URLCONF = "ibvl.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["ibvl/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ],
        },
    },
]

WSGI_APPLICATION = "ibvl.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {"default": dj_database_url.parse(DB)}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:3002",
    "http://localhost:3003",
    "http://localhost:3123",
    "http://" + DOMAIN,
    "https://" + DOMAIN,
    "http://" + DOMAIN + ":3000",
    "https://" + DOMAIN + ":3000",
    "http://" + DOMAIN + ":8000",
    "https://" + DOMAIN + ":8000",
]


# for the "View Site" link in admin dashboard toolbar
if isinstance(os.environ.get("FRONTEND_URL"), str):
    SITE_URL = os.environ.get("FRONTEND_URL")
else:
    SITE_URL = "https://" + DOMAIN
    

# Authentication
CSRF_COOKIE_SAMESITE = "Strict"
SESSION_COOKIE_SAMESITE = "Strict"
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_HTTPONLY = True
CSRF_TRUSTED_ORIGINS = CORS_ALLOWED_ORIGINS

if DEBUG:
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
            },
        },
        "root": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
    }
else:
    LOGGING = {}
