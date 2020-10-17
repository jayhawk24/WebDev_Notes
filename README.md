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
