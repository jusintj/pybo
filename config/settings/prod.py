from .base import *

ALLOWED_HOSTS = ['43.202.27.5']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'dbmasteruser',
        'PASSWORD': 'rlaxowls76$',
        'HOST': 'ls-2a5af5c191149decef67c243cb9074e4a92018c9.cf4m8y8aqfa5.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}