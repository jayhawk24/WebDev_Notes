# Mordern Web Technologies Courses Notes

## Django
- Django Project is a collection if application and configurations that when combined together will make up the full web application.
- A django application is created to perform a particular functionality for our entire web application. like polling app, comments app. etc..
- They are reusable or plugable django apps.


### Init Commands
```
    python3 -m venv proj-name
    source bin/activate
    pip3 install django
    django-admin startproject name
```

#### Config files

- __init__.py
  - Blank python script that due to its special name let's python know that his directory can be treated as a package.
- settings.py
    - this is where we store project settings.
- urls.py
    - stores all the URL patterns for your project . Basically the different pages of your web application.
- wsgi.py
  - This script acts as the web server gateway interface. it wil later on help us deploy our web app to production.
- manage.py
  - most used
  - It will be associated with many commands .


#### Migration
- migration allows us to move databases from one design to another, this is also reversible.
- So we can migrate our database

### App starting commands
```
  python manage.py startapp first_app

```
#### App files
- apps.py
  - here we place application specific configurations.
- models.py
  - here we store applications data model.
- tests.py
  - here we can store test functions to test our code.
- views.py
  - this is where we have functions that handle requests and return responses
- Migrations folder
  - stores database specific information as it relates to the models

#### Steps To Add an App
- First start an app.
- add app name under settings.py file.
- in views.py file import HttpResponse from django.http.
- create a function in views.py called index.
- add URL in url pattern .
  
### URL Mapping
- create a urls.py file inside app directory which is same as urls.py file in project directory
- include app.urls.py file in project.urls.py file
  ```
  from django.conf.urls import 
  urlpatterns = [
    path('yourpath/',include('app.urls')),
  ]
  ```
- include views in app.urls.py file
### Add Template
- add template directory in settings.py after creating a template directory
  
  ```
  import os
  TEMPLATE_DIR = os.path.join(BASE_DIR,"template's_foldername")
  ```

- Then create index.html in template folder use {{ insert_me }} to inject dictionary variables.
- go to views.py in first_app and use this function
  ```
  def index(request):
    myDict = {"insert_me":"This is injected to index.html"}
    return render(request,'first_app/index.html',context=myDict)
  ```

### Add Static files
- Add STATIC_DIR variable in project.settings.py as the path for static directory.
- At the bottom add STATICFILES_DIRS = [STATIC_DIR,] 
- In index.html below doctype html add template tag as below
  ```
  {% load static %}
  <link rel="stylesheet" href="{% static 'css/style.css'%}">
  ```

### Add Models
- to add models we first define classes in models.py file in first_app directory as table names and inside variables as columns like
  ```

  class Webpage(models.Model):
      topic = models.ForeignKey(Topic, on_delete=models.CASCADE,)
      name = models.CharField(max_length=256, unique=True)
      url = models.URLField(unique=True)

      def __str__(self) -> str:
          return self.name
  ```
- Then run command
  ```
  python3 manage.py migrate

  python manage.py makemigrations first_app
  python manage.py migrate
  ```

### Add Admin Page
- import all models from models.py
- use this command to register
  ```
  from first_app.models import *

  admin.site.register(modelname)
  ```
- create a super user
- python3 manage.py createsuperuser

### Connecting Models, Templates, Views
- In views.py file we import any models that we will need to use.
- Use the view to query the model for data that we will need
- pass results from the model to the template.
- Edit template so that it is ready to accept and display the data from the model.
- Map a url to the view.