from os import path


BASE_DIR = path.dirname(path.dirname(__file__))

PROJECT_PATH = path.realpath(path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '51s13)ne_+7%%y0npc-lw9u*e58q9o#&^%g7c60udrw*qd2611'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'

DEFAULT_EMAIL = 'dafot.webtech@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'dafot.webtech'
EMAIL_HOST_PASSWORD = 'rwthaachenuniversity'
EMAIL_USE_TLS = True

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.static',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.debug',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',
    'web_portal.core.form_messages',
    'web_portal.core.courses',
    'web_portal.core.users',
    'registration',
    'macros',
    'widget_tweaks',
    'django_markdown2',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'web_portal.urls'

WSGI_APPLICATION = 'web_portal.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'databasename',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'host',
        'PORT': 'port',
    }
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher',
)

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    PROJECT_PATH + '/static/',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = path.join(PROJECT_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT.
MEDIA_URL = '/media/'

# Activation period for new user
ACCOUNT_ACTIVATION_DAYS = 7

TEMPLATE_DIRS = (
    PROJECT_PATH + '/templates/',
)

# External Web Service information
SERVER_URL = 'http://codeservice.herokuapp.com'
REST_API = SERVER_URL + '/rest'

# Supported solution languages
LANGUAGES = (
    ('python', u'Python'),
    ('java', u'Java')
)