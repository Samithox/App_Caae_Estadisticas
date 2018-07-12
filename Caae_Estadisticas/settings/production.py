from Caae_Estadisticas.settings.base import *
import os
 

DEBUG = False
#TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'reportes',                      # Or path to database file if using sqlite3.
        'USER': 'caae',                      # Not used with sqlite3.
        'PASSWORD': '@CAAE.2018',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

COMPRESS_OFFLINE = True

ALLOWED_HOSTS = ['localhost','172.0.0.0']