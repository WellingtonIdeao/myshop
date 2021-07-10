from .base import *
import environ
import braintree

environ.Env.read_env()
env = environ.Env(
    DEBUG=(bool, True)
)
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': env.db(),
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Braintree settings
BRAINTREE_MERCHANT_ID = env('BRAINTREE_MERCHANT_ID')  # Merchant ID
BRAINTREE_PUBLIC_KEY = env('BRAINTREE_PUBLIC_KEY')  # Public Key
BRAINTREE_PRIVATE_KEY = env('BRAINTREE_PRIVATE_KEY')  # Private key

BRAINTREE_CONF = braintree.Configuration(
    braintree.Environment.Sandbox,
    BRAINTREE_MERCHANT_ID,
    BRAINTREE_PUBLIC_KEY,
    BRAINTREE_PRIVATE_KEY
)


