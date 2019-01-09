import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '%$v+=c=vs04ya=o61e701!64i78zxm0ho+3y1nlf!a6m8c77wq'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'django.contrib.sites', # django-eav
  'django_extensions',
  #'eav',
  'corsheaders',
  'django_jinja',
  'rest_framework',
  #'crispy_forms', # django-crispy-forms
  'bootstrap3', # django-bootstrap3
  'api',
  'mptt',
]

MIDDLEWARE_CLASSES = [
  'corsheaders.middleware.CorsMiddleware',
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
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
  }, {
    'BACKEND': 'django_jinja.backend.Jinja2',
    'APP_DIRS': True,
    
    'OPTIONS': {
      #'match_extension': None,
      'match_extension': '.jinja',
      
      'context_processors': [
          'django.contrib.auth.context_processors.auth',
          'django.template.context_processors.debug',
          'django.template.context_processors.i18n',
          'django.template.context_processors.media',
          'django.template.context_processors.static',
          'django.template.context_processors.tz',
          'django.contrib.messages.context_processors.messages',
      ],
    },
  },
]

WSGI_APPLICATION = 'main.wsgi.application'

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
  }
}

AUTH_PASSWORD_VALIDATORS = [
  {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
  {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
  {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
  {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/assets/'
# STATIC_ROOT = 'staticfiles'  # for heroku
MEDIA_ROOT = 'media'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'staticfiles')]

REST_FRAMEWORK = {
  # 'DEFAULT_PERMISSION_CLASSES': [
  #   'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
  # ],
  
  'PAGE_SIZE': 100,
  
  #'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',), # django-filter
  'DEFAULT_FILTER_BACKENDS': ('rest_framework_filters.backends.DjangoFilterBackend',), # djangorestframework-filters
}

#CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = ['localhost']
#CRISPY_TEMPLATE_PACK = 'bootstrap3' # django-crispy-forms
SITE_ID = 1
SHELL_PLUS = 'plain'

SHELL_PLUS_POST_IMPORTS = (
  ('api', ('models', 'forms', 'admin')),
)

#APPEND_SLASH = False # URL routing
