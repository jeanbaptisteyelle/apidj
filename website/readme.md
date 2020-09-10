
Installation 

sudo snap install --classic heroku

pip install whitenoise

pip install gunicorn

pip install django_heroku


creation du fichier Procfile
    web: gunicorn nom_projet.wsgi

faire requirements

python manage.py collectstatic


ALLOWED_HOSTS = ['*']
import django_heroku

django_heroku.settings(locals())
