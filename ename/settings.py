"""
Django settings for ename project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '80u0vbfv-kvx5h6j8d=gac89&bwg_n%_e!g^9vxoff)jbhbs*+'

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

    'www',
    'name',
    'api',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ename.urls'

WSGI_APPLICATION = 'ename.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'app_ename',
        'USER': 'root', 
    }
}

TEMPLATE_DIRS = (                                                              
    BASE_DIR + "/templates",                            
    BASE_DIR + "/libs/djangorestframework/templates",   
)             

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Hong_Kong'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

MEDIA_ROOT = BASE_DIR + '/media/'
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

ENAME_URLS = [
        'http://www.behindthename.com/names/usage/english/1',
        'http://www.behindthename.com/names/usage/english/2',
        'http://www.behindthename.com/names/usage/english/3',
        'http://www.behindthename.com/names/usage/english/4',
        'http://www.behindthename.com/names/usage/english/5',
        'http://www.behindthename.com/names/usage/english/6',
        'http://www.behindthename.com/names/usage/english/7',
        'http://www.behindthename.com/names/usage/english/8',
        'http://www.behindthename.com/names/usage/english/9',
        'http://www.behindthename.com/names/usage/english/10',
        'http://www.behindthename.com/names/usage/english/11',
        'http://www.behindthename.com/names/usage/english/12',
        'http://www.behindthename.com/names/usage/english/13',
    ]

TRANSLATE_URL = 'http://dict.youdao.com/search?le=eng&q='
MP3_URL = 'http://dict.youdao.com/dictvoice?audio='
CNAME_URL = 'http://ename.dict.cn/'

PINYIN_DICT = BASE_DIR + '/data/word.data'
ROMA_FILE = BASE_DIR + '/data/roma'

FUXING_LIST = [
    u'\u8f69\u8f95',
    u'\u6b27\u9633',
    u'\u53f8\u9a6c',
    u'\u53f8\u5f92',
    u'\u53f8\u7a7a',
    u'\u53f8\u5bc7',
    u'\u4e0a\u5b98',
    u'\u5c09\u8fdf',
    u'\u7f8a\u820c',
    u'\u7b2c\u4e94',
    u'\u6881\u4e18',
    u'\u949f\u79bb',
    u'\u4e1c\u90ed',
    u'\u516c\u5b59',
    u'\u5b5f\u5b59',
    u'\u4ef2\u5b59',
    u'\u53d4\u5b59',
    u'\u5b63\u5b59',
    u'\u957f\u5b59',
    u'\u6155\u5bb9',
    u'\u5b87\u6587',
    u'\u95fe\u4e18',
    u'\u8bf8\u845b',
    u'\u4e1c\u65b9',
    u'\u7384\u6781',
    u'\u4e1c\u95e8',
    u'\u897f\u95e8',
    u'\u516c\u7f8a',
    u'\u590f\u4faf',
    u'\u4e07\u4fdf',
    u'\u767e\u91cc',
    u'\u7aef\u6728',
    u'\u516c\u51b6',
    u'\u7687\u752b',
    u'\u547c\u5ef6',
    u'\u6d6e\u5c60',
    u'\u4ee4\u72d0',
    u'\u6df3\u4e8e',
    u'\u5373\u58a8',
    u'\u5355\u4e8e',
    u'\u5357\u5bab',
    u'\u7530\u4e18'
    ]
