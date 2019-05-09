## Backend 

Python 3.7.3

Django 2.2


set PATH=%PATH%;C:\your\path\here\


Django

Creating a project:

django-admin startproject mysite

Goal:
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py

The development server:
cd mysite
python manage.py runserver

Goal:
http://127.0.0.1:8000/


An app is a Web application that does something – e.g., a Weblog system, a database of public records or a simple poll app. 

A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

Creating the Polls app

python manage.py startapp polls

Goal:
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py

