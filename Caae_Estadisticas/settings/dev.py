import os
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ROOT_PATH = os.path.join(os.path.dirname(__file__), '..')

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ROOT_PATH, 'db.sqlite3'),
    }
}