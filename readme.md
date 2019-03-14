**Install postgre-sql and create database and user.**

sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib

sudo su - postgres

psql

CREATE DATABASE to_do_database;

CREATE USER to_do_user WITH PASSWORD 'password';

ALTER ROLE to_do_user SET client_encoding TO 'utf8';

ALTER ROLE to_do_user SET default_transaction_isolation TO 'read committed';

GRANT ALL PRIVILEGES ON DATABASE to_do to to_do_user;

**Create environment and install dependencies. **

python3 -m venv ~/.virtualenvs/to_do_env

source ~/.virtualenvs/to_do_env/bin/activate

pip install django

pip install django psycopg2

pip install celery

sudo apt-get install redis-server

**Clone the project.**

**MAKE INITIAL MIGRATIONS**

cd ~/to_do

python manage.py makemigrations

python manage.py migrate

python manage.py migrate djcelery

**CREATE SUPERUSER**

python manage.py createsuperuser

**Run server**

python manage.py runserver

**Run Celery worker**

celery -A to_do worker -B


