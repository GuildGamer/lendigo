#!/bin/bash

echo "MAKE MIGRATIONS"
python manage.py makemigrations

echo "START SERVER"
python manage.py runserver 0.0.0.0:8000 &

echo "STARTTING CELERY BEAT"
celery -A Ledingo_challenge beat -l info --logfile=celery.beat.log --detach

echo "STARTTING CELERY WORKER"
celery -A Ledingo_challenge worker -l info --logfile=celery.log --detach