
from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-x$c$=pn&(e(&g6e$=q92++g8n@-i=kh21uzj*17*((m2h&=j1#'

DEBUG = True

ALLOWED_HOSTS = []



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_spectacular',
    'f1_manage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'projetoFabricaDeSoftware.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'projetoFabricaDeSoftware.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'f1_database',
        'USER': 'root',
        'PASSWORD': config('SENHA_DB'),
        'HOST': config('HOST_DB'),
        'PORT': config('PORT_DB'),
    }
}



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'


MAILERS = {
    'default': {
        'BACKEND': 'django.core.mail.backends.console.EmailBackend',
    },
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'F1 Management API',
    'DESCRIPTION': '''
API REST para gerenciamento de pilotos e equipes de Fórmula 1.

A API permite:

• Cadastrar pilotos
• Consultar pilotos
• Atualizar pilotos
• Remover pilotos
• Cadastrar equipes
• Consultar equipes
• Atualizar equipes
• Remover equipes
• Consultar informações da Fórmula 1 através da OpenF1 API
    ''',
    'VERSION': '1.0.0',

    'SERVE_INCLUDE_SCHEMA': False,

    'TAGS': [
        {
            'name': 'Pilotos',
            'description': 'Operações relacionadas aos pilotos de Fórmula 1.'
        },
        {
            'name': 'Equipes',
            'description': 'Operações relacionadas às equipes de Fórmula 1.'
        },
        {
            'name': 'OpenF1',
            'description': 'Consultas de dados externos através da OpenF1 API.'
        },
    ],
}

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}