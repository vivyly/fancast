from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Vivien Yang', 'vivyly9@gmail.com'),
)

MANAGERS = ADMINS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fancast',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}