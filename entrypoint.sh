#!/bin/sh

echo "running migrations"
python manage.py makemigrations
python manage.py migrate

echo "Apply database migrations"
gunicorn main.wsgi --bind 0.0.0.0:8000
exec "$@"