DATABASES = {
 'default': {
 'ENGINE': 'django.db.backends.mysql',
 'NAME': 'mysite_db',
 'USER': 'mysite_usr',
 'PASSWORD': 'mysite_pass',
 }
}


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
