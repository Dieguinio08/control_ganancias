#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

DJANGO_SUPERUSER_PASSWORD=$SUPER_USER_PASSWORD python manage.py createsuperuser --username $SUPER_USER_NAME --email $SUPER_USER_EMAIL --noinput
python manage.py makemigrations
python manage.py migrate

# Init DB
python manage.py init_f1357
python manage.py init_deducciones
python manage.py init_conceptos
python manage.py init_tablas_d
python manage.py init_tablas

gunicorn ganancias_pr.wsgi:application --bind 0.0.0.0:8000