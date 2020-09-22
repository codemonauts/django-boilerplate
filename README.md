# Django-Boilerplate

Use this as a starting point for new Django projects. This boilerplate is intendet to represent our way of developing
Djang so we made some decisions in this repository:

    - Custom user model
    - Use pug instead of plain HTML
    - Move apps into the project folder
    - User one globale template folder for all apps
    - Use AWS S3 to store assets in production
    - Different settings files for different stages
    - Docker/Docker-Compose for local development
    - gulp.js for css/js/image processing

# Usage
Make sure you have Docker and docker-compose installed. Then execute the following steps to create a project with the
name *myproject*:
```
mkdir myproject && cd myproject
django-admin startproject --template https://github.com/codemonauts/django-boilerplate/archive/main.zip --name=docker-compose.yml myproject .
docker-compose up
```
Your new Django installation should now be reachable at [localhost:8000](http://localhost:8000)

## Install new dependencies
```
echo "libraryname" >> requirements.txt
docker-compose exec web pip install -r requirements.txt
```

## Run Django comamands with manage.py
```
docker-compose exec web ./manage.py <command>
```

## Import DB dump
The dump must be located inside the project dir
```
docker-compose exec db import <filename>
```

## Create a DB dump
```
docker-compose exec db dump
```
