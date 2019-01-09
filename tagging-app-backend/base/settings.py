import os
#import posixpath

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'f2415cfe-945d-4478-bfd9-d07fdb74f232'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    # Local apps:

    'base',


    # Third-party apps:

    'corsheaders',
    'django_extensions',
    'django_filters',
    'mptt',
    'rest_framework',
    'rest_framework_filters',


    # Django apps:

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'base.urls'

TEMPLATES = [{
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
}]

WSGI_APPLICATION = 'base.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    #{'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    #{'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    #{'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    #{'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/app-static/'

#MEDIA_URL = '/app-media/'

#STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static']))
#MEDIA_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['media']))

API_PAGE_SIZE = 100

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],

    'PAGE_SIZE': API_PAGE_SIZE,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',

    #'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.DjangoModelPermissions',),
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',),

    'DEFAULT_FILTER_BACKENDS': (
        #'rest_framework_filters.backends.ComplexFilterBackend',
        #'rest_framework_filters.backends.DjangoFilterBackend', # djangorestframework-filters
        #'rest_framework.filters.OrderingFilter',
        'url_filter.integrations.drf.DjangoFilterBackend',
    ),
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

SHELL_PLUS_POST_IMPORTS = [
    ('base', 'util'),
    ('pprint', 'pprint'),
]
