import jinja2
import os
import pydash as _; _.map = _.map_; _.filter = _.filter_; _.zip = _.zip_


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
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
  'app',
  'django_extensions',
  'django_jinja',
  'eav',
  'mptt',
  'rest_framework',
]

MIDDLEWARE_CLASSES = [
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'


class CustomJinja2Environment(jinja2.Environment):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.finalize = lambda val: '' if val == None else val


TEMPLATES = [
  {
    'BACKEND': 'django_jinja.backend.Jinja2',
    'APP_DIRS': True,
    
    'OPTIONS': {
      'environment': 'settings.CustomJinja2Environment',
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
      
      'globals': {
        '_': _,
        'getattr': getattr,
        'dir': dir, # Debug
        'locals': locals, # Debug
      },
      
      'filters': {
        'json': 'json.dumps',
      },
    },
  },
  
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

WSGI_APPLICATION = 'wsgi.application'

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
  },
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
STATIC_URL = '/static/'
MEDIA_URL =  '/media/'
MEDIA_ROOT = 'media'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'staticfiles')]
# STATIC_ROOT = 'staticfiles' # for heroku

REST_FRAMEWORK = {
  'DEFAULT_AUTHENTICATION_CLASSES': [
    'rest_framework.authentication.BasicAuthentication',
    'rest_framework.authentication.SessionAuthentication',
  ],
  
  'DEFAULT_PERMISSION_CLASSES': [
    'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
  ],
  
  # 'DEFAULT_RENDERER_CLASSES': [
  #   'rest_framework.renderers.StaticHTMLRenderer',
  # ],
  
  # 'PAGE_SIZE': 10,
  'DEFAULT_FILTER_BACKENDS': ('rest_framework_filters.backends.DjangoFilterBackend',), # djangorestframework-filters
}

AUTH_USER_MODEL = 'app.User'
# CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = ['localhost']
# CRISPY_TEMPLATE_PACK = 'bootstrap3' # django-crispy-forms
SITE_ID = 1
SHELL_PLUS = 'plain'

SHELL_PLUS_POST_IMPORTS = (
  'json',
  ('app', 'models'),
  ('django.conf', 'urls'),
  ('django.contrib', 'auth'),
  ('django.core', 'urlresolvers'),
  ('pprint', 'pprint'),
  ('rest_framework', ('renderers', 'parsers')),
)
