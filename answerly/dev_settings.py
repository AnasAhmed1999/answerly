from .common_settings import *

DEBUG = True
SECRET_KEY = 'some secret'


DATABASES['default'].update({
    'NAME': 'mymdb',
    'USER': 'mymdb',
    'PASSWORD': 'development',
    'HOST': 'localhost',
    'PORT': '5432'
})
