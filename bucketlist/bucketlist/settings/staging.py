"""
Staging specific settings for bucketlist project.
"""

import dj_database_url
import os

from .base import *


APPLICATION_DIR = os.path.dirname(globals()['__file__'])

DEBUG = False

DATABASES = {
    'default': dj_database_url.config()
}

# Enable Connection Pooling
DATABASES['default']['ENGINE'] = 'django_postgrespool'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']
