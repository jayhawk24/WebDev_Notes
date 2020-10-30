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

### Script to populate models
```
from faker import Faker
import os
import django

django.setup()


from apptwo.models import *

fakegen = Faker()


def populate(N=10):
    for entry in range(N):
        print(5)
        fname = fakegen.name().split()[0]
        lname = fakegen.name().split()[0]
        email = fakegen.email()

        us = User.objects.get_or_create(
            firstName=fname,
            lastName=lname,
            email=email
        )[0]

if __name__ == "__main__":
    print("Running scripts")
    populate(int(input("Number of data to be added.")))
```

### Adding forms
- Add form view function in views.py file
  
```
  def formview(request):
    form = forms.formName()

    if request.method == 'POST':
        form = forms.formName(request.POST)

        if form.is_valid():
            print("Validation success")
            print("Name : "+form.cleaned_data["name"])
            print("Email : "+form.cleaned_data["email"])
            print("Text : "+form.cleaned_data["text"])

    return render(request,'forms.html',{'form':form})
```
- add this view to urls.py file
- In forms.html file create a form using
```
{{form.as_p}}
{% csrf_token %}
```
### Saving Data from forms
- create a forms.py file inside app. import models
```
  from django import forms
  from apptwo.models import User


  class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
```
- Now inside views.py file import Newuserform class created in forms.py file

```

def signup(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Invalid Form")
    
    return render(request,'signup.html',context={'form':form})
  
```

### Templating Urls
- {% url 'basic_app:other' %} in html page
- where basic_app is a variable assigned as app_name inside urls.py file in app folder
- and other is the name of the page to be directed to it.
- this name should be defined in urls.py file
- path('other', views.other, name="other"),
  
### Template Inheritance
- in your base.html file put up all the stuff you would like to inherit and at bottom inside a div container add a template tag
```
        {% block body_block %}

        {% endblock %}
```
- now in your rest of HTML file all you need to to is after declaring doctype give this
```
    {% extends "basic_app/base.html" %}
    
    {% block body_block %}

    <h2>Welcome to other</h2>
    
    <h3>Inherited </h3>
    {% endblock %}
```
### Saving Username and passwords
- Create a model which will inherit default User model which contains username and password fields.
  ```
  from django.db import models
  from django.contrib.auth.models import User

  class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    
    portfolioSite = models.URLField(blank=True)

    profilePic = models.ImageField(upload_to='profilePics', blank=True)

    def __str__(self) -> str:
        return self.user.username
  ```
- Add Password hashers in settings.py 
```
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]
```
- In forms.py file 
```
from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from basic_app.models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ("username","email","password")


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolioSite','profilePic')
```
- In views.py file create a function to save data 
```
from django.http import request
from basic_app.forms import UserForm,UserProfileInfoForm
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def register(request):
    
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            registered = True
    
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'registration.html',
                {'user_form':user_form,
                'profile_form':profile_form,
                'registered':registered}
    )
```
- In registration.html file
```
<!DOCTYPE html>
{% extends 'base.html' %}

{% load static %}

{% block body_block %}

    <div class="jumbotron">
        {% if registered %}
        <h1> Thank you for registering!</h1>
        {% else %}
        <h3> Fill out the form : </h3>

        <form method="POST" enctype="multipart/form-data">
            {% csrf_token %}
            {{ user_form.as_p}}

            {{ profile_form.as_p }}
            <input type="submit" name="" value="Register">


        </form>     
        {% endif %}

    </div>
{% endblock  %}
```
### Including User Login
- imports and functions in views.py
```

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


def user_login (request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account not active")

        else:
            print("Someone tried to login and failed!")
            print("username: {} and password {}".format(username,password))
            return HttpResponse("Invalid Login details supplied!")
    
    else:
        return render(request,'login.html',{})

```
- In login.html
```
{% extends 'base.html' %}

{% block body_block %}

<div class="jumbotron">
    <h1>Please Login
    </h1>
    <form action="{% url 'user_login' %}" method="POST">
        {% csrf_token %}

        <label for="username">Username:</label>
        <input type="text" name="username" placeholder="Enter Username">

        <label for="password">Password:</label>
        <input type="password" name="password">

        <input type="submit" name="" value="Login">
        
    </form>
</div>

{% endblock  %}
```

### Class Based Views
- We have to first import from jango.views.generic View and TemplateView and then create a class.
- ```
  from django.views.generic import View,TemplateView

  class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
      context = super().get_context_data(**kwargs)
      context['tobeinjected'] = "basic injection"
      return context

  ```
- Then in urls.py file we declare it as...
- ```path("", views.IndexView.as_view())```

#### List view and detail view
- Say we have 2 models namely school and students.
- we can list the views as...
```
from django.views.generic import View,TemplateView,ListView,DetailView

class schoolListView(ListView):
  model = models.School

  # this returns context dictionary as school_list by default
  # to change name we can do 
  context_object_name = "schools"


class schoolDetailView(DetailView):
  model = models.School
  template_name = 'school.html'


```
