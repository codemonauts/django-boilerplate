from .common import *


SECRET_KEY = ""
DEBUG = False

STATIC_ROOT = os.path.join(BASE_DIR, "../static")
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

DATABASES = {
    "default": {"ENGINE": "django.db.backends.mysql", "NAME": "", "USER": "", "PASSWORD": "", "HOST": "", "PORT": 3306}
}
