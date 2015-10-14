#coding=utf-8   # 添加此头文件，中文注释才不会报错
"""
Django settings for test9_29 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k#brk41wo4ysf%o0m_xyo=ar8#0-4e=8s+8#k4^a$q8395y6o5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    # 'debug_toolbar',
    # 'debug_toolbar.apps.DebugToolbarConfig',#django-debug-toolbar
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


ROOT_URLCONF = 'test9_29.urls'

WSGI_APPLICATION = 'test9_29.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 连接数据库所用的驱动
        'NAME': '16srna_db1',                        # 所连接的数据库的名字
        'USER':'root',                          # 所连接的数据库的用户名
        'PASSWORD':'xiezongzheng',            # 数据库密码
        'Host':'127.0.0.1',                    # 数据库IP地址
        'PORT':'3306',                          # 端口
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = ''
STATICFILES_DIRS = (os.path.join(os.path.dirname(__file__), '../static/').replace('\\','/'),)

TEMPLATE_DIRS = (os.path.join(BASE_DIR,  'templates'),)



