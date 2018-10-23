"""
Django settings for Estadisticas project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
from os.path import abspath, dirname, join
from django.conf import global_settings

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_ROOT = dirname(dirname(dirname(abspath(__file__))))

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+#&#&cntj)ql_7&7$(2wn4!ltvd+@-pdbm#+g6df92%2#7f!e='

# SECURITY WARNING: don't run with debug turned on in production!




# Application definition

INSTALLED_APPS = (
    #'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
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



ROOT_URLCONF = 'Caae_Estadisticas.urls'

WSGI_APPLICATION = 'Caae_Estadisticas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases



# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            join(PROJECT_ROOT, 'templates')
        ],
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

#AUTH_PROFILE_MODULE = 'Profile.Profiles'
STATIC_URL = '/static/'

STATIC_ROOT = "C:\inetpub\wwwroot\App_Caae_Estadisticas/app\static"



MEDIA_ROOT = join(PROJECT_ROOT, 'reportes')
MEDIA_URL = '/reportes/'


LOGIN_REDIRECT_URL = '/'


try:
    from Caae_Estadisticas.settings.production import  *
except ImportError:
    pass
