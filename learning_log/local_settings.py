from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4j8e&x*lb0d772w@w*c3bz3c5qgy0vf^p^x$c=&^z=iwn17(i2'

DEBUG = True

ALLOWED_HOSTS = []



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Настройки django-bootstrap3
BOOTSTRAP3 = {
        'include_jquery': True,
}

STATIC_URL = 'static/'