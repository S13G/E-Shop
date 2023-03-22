import dj_database_url

from .settings import *

SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG", False, cast = bool)

ALLOWED_HOSTS = [
    "link"
]

CSRF_TRUSTED_ORIGINS = ["https://" + host for host in ALLOWED_HOSTS]

# DATABASES = {"default": dj_database_url.config()}
DATABASES = {
    "default": dj_database_url.parse(
        config("DB_URL", ""),
        conn_max_age=600,
        conn_health_checks=True,
    )
}

INSTALLED_APPS.remove("debug_toolbar")
MIDDLEWARE.remove("debug_toolbar.middleware.DebugToolbarMiddleware")

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": config("CLOUD_NAME", ""),
    "API_KEY": config("CLOUD_API_KEY", ""),
    "API_SECRET": config("CLOUD_API_SECRET", ""),
}


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST= 'smtp.gmail.com'
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD =config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_SSL = False
EMAIL_USE_TSL = True




