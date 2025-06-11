DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'host.docker.internal',  # This allows access to host's MySQL from container
        'PORT': '3306',
    }
}

