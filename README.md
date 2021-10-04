## Directory Structure

    1) "Assignment" contains:
            a) web servers
            b) settings for the project
            c) urls.py which includes all App's urls.py
    2) "theorem" is the App for this project
            a) "management" contains management commands for the App
            b) "migration" holds all database design changes from time to time
            c) "templates" holds all templates w.r.t this App.
            c) "models.py" holds the database blueprint.
            c) "views.py" has all the view functions for the App.
    3) "production_static" holds the static files of all Apps in this project
    4) "static" directory gets created when you run collectstatic and all static files are served from here.
    5) "templates" directory holds all base templates for the project.
    
## Create a virtual environment and install dependencies

    $ python3 -m venv .virtualenvs/assignment
    $ source /home/ubuntu/.virtualenvs/assignment/bin/activate
    $ pip install -r requirements.txt

## Migrate database Models and load static files and csv data

    $ python manage.py migrate
    $ python manage.py collectstatic

## Run the server on localhost at 8000 port
    
    $ python manage.py runserver 0.0.0.0:8000
