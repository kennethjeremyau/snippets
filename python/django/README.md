# Django example

A sample Django application.

## Installation
1. Create virtual environment.
```bash
python3 -m venv venv
pip3 install -r requirements.txt
source venv/bin/activate
```
1. Create new django application.
```bash
# Adding the . ensures we don't have the nested newproject/newproject issue.
django-admin startproject newproject .
# Identical to `django-admin startapp newapp1`.
python3 manage.py startapp newapp1
```

## Activate
Activate the virtual python environment so we are using the correct installed dependencies.
```bash
source venv/bin/activate
```

## Deactivate
Deactivate the virtual python environment.
```bash
deactivate
```

## Run server locally
```bash
python3 manage.py runserver
```
