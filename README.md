
# airportapp-django-drf-postgresql

first create your virtualenv

`$ python3 -m venv venv`

activate venv

`$ source venv/bin/activate`

then install requeriments

`$ pip install -r requirements.txt`

install postgresql, login and create the database

`CREATE DATABASE airportapp`

create a .env file

`$ touch .env`

and add your postgresql credentials and the app SECRET_KEY to .env file

>ENV_SECRET_KEY="{add a secret key like bhajfbkjhawbdkjhabdjh}"
ENV_NAME='airportapp'
ENV_HOST='{your host or localhost}'
ENV_PORT='{your db port or 5432}'
ENV_USER='{your db user}'
ENV_PASSWORD='{your db password}

finally the project run with:
`$ python manage.py runserver`


