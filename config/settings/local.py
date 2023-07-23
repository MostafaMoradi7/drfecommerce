import os

from django.conf import settings

from .base import *

os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.local"
settings.configure()


BASE_DIR_FOR_DB = BASE_DIR.parent
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR_FOR_DB / "db.sqlite3",
    }
}
