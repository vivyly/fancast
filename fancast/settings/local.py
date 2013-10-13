import os
from .base import *

ROOT = os.path.abspath(os.path.dirname(__file__))

ADMINS = (
    ('Vivien Yang', 'vivyly9@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ROOT, 'fancast.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


# You might want to use sqlite3 for testing in local as it's much faster.
if len(sys.argv) > 1 and 'test' in sys.argv[1]:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '/tmp/fancast_test.db',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
    }
