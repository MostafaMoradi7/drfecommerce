from .base import * 
BASE_DIR_FOR_DB = BASE_DIR.parent
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR_FOR_DB / 'db.sqlite3',
    }
}