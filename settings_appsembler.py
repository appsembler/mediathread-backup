import os.path
from settings import *

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    #'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'mediathread_main.views.django_settings',
    )

EXTRA_INSTALLED_APPS = (
    'django.contrib.staticfiles',
    )

# add any extra apps to the INSTALLED_APPS
try:
    INSTALLED_APPS = tuple(list(INSTALLED_APPS) + list(EXTRA_INSTALLED_APPS))
except NameError:
    pass

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, "templates"),
)

# original media assets are copied from the media directory
STATICFILES_DIRS = (
     os.path.join(PROJECT_ROOT, 'media/'),
)

# static media is collected to the directory site_media
STATIC_ROOT = os.path.join(PROJECT_ROOT, "site_media")
STATIC_URL = '/site_media/'

MEDIA_ROOT = os.path.join(PROJECT_ROOT, "uploads")
MEDIA_URL = '/uploads/' # same as in settings_shared.py, just to keep both settings together


DEBUG = False
TEMPLATE_DEBUG = DEBUG

WIND_SERVICE = "cnmtl_full_p"

try:
    from local_settings import *
except ImportError:
    pass

