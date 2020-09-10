
INSTALLATION

    sudo snap install --classic heroku

    pip install whitenoise

    pip install gunicorn

    pip install django_heroku

CONFIGURATION

    création du fichier Procfile
        web: gunicorn nom_projet.wsgi


    ALLOWED_HOSTS = ['*']


    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    MIDDLEWARE = [
        #...
        'whitenoise.middleware.WhiteNoiseMiddleware'
    ]


    STATICFILES_DIRS = [
        #...
    ]

    import django_heroku

    django_heroku.settings(locals())

PROCEDURE DU LANCEMENT

    faire un requirements

        pip freeze > requirements .txt

    python manage.py collectstatic
