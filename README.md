# Django Web Development
Using free template following functions are created \
* connection to postgresql
* Register user \
* login
* logout
* dynamic content display from database

## 
There is one project file and multiple apps in that project

## Basic commands 
```bash
django-admin startproject name
django-admin startapp name
python manage.python runserver
```

## Files 
### View 
this file has all the backend functions of a webpage

### URLS
this file maps the url/webpages to their respective functions

### Models
Represents table in our DB \
every attribute of the class is a field of the table

### Templates folder
we can save all the webpages in this one folder \
generally it is known as templates

# Foobar

Foobar is a Python library for dealing with word pluralization.
* Create Project
```bash
django-admin startproject myproject
```
* create application 
```bash
python manage.py startapp appname
```
* in main project's url file add
 ```python 
from django.conf.urls import url, include
url('', include('application_name.urls'))
```
* For html pages
  * Create a folder in main project called "templates" (for wabpages, any name can be given to foler)
  * In settings.py of main project, find "TEMPLATES" 
edit "'DIRS': []"
```python
# for windows
# templates is (html pages folder name)
'DIRS': [os.path.join(BASE_DIR,'templates')] 
```
```python
# for linux
# templates is (html pages folder name)
'DIRS': ['project_name/templates'] 
```
* Write function inside views.py of application
```python
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')
```

* create urls.py in application folder
```python
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url('', views.home, name='home'),
    url('#', views.#, name='#') # add multiple pages and link to url
]
```
