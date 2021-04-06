from pathlib import Path

import environ


MODULE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = MODULE_DIR.parent

env = environ.Env()
env.read_env(env_file=str(PROJECT_DIR.joinpath('.env')))

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG', default=False)

ALLOWED_HOSTS = ['*']

CACHE = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': str(MODULE_DIR.joinpath('cache'))
    }
}

INSTALLED_APPS = [
    # System modules
    'pizzaria.modules.core.CoreConfig',
    'pizzaria.modules.domain.DomainConfig',
    'django.contrib.messages'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pizzaria.urls'

WSGI_APPLICATION = 'pizzaria.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT', default='5432')
    }
}

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Bahia'

USE_I18N = False

USE_L10N = False

USE_TZ = False

DATE_INPUT_FORMATS = ['%Y-%m-%d']

DATETIME_INPUT_FORMATS = ['%Y-%m-%d %H:%M:%S']

TIME_INPUT_FORMATS = ['%H:%M']
