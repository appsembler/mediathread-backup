import os.path
from mediathread.settings import *

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    #'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'mediathread_main.views.django_settings',
    )

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, "templates"),
)

MEDIA_ROOT = os.path.join(PROJECT_ROOT, "uploads")
MEDIA_URL = '/uploads/' # same as in settings_shared.py, just to keep both settings together

DEBUG = False
TEMPLATE_DEBUG = DEBUG

WIND_SERVICE = "cnmtl_full_p"

try:
    from local_settings import *
except ImportError:
    pass

