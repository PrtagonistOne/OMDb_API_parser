#!/bin/sh


if [ "$DATABASE" = "postgres" ]
    then
        echo "Waiting for postgres..."

        while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
        done

        echo "PostgreSQL started"
    fi



# shellcheck disable=SC2164
cd omdb/
pytest
python manage.py runserver 0.0.0.0:7000