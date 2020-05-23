from .common import *


SECRET_KEY = '*,Ur4R&~Z=kp7~j1(Lh0k,4/hF3Y$QxEtpC"<3CbAcx<yqT39x'
DEBUG = False

STATIC_ROOT = os.path.join(BASE_DIR, "../static")
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": 3306,
    }
}
