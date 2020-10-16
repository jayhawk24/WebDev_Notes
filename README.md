# Mordern Web Technologies Courses Notes

## Django
- Django Project is a collection if application and configurations that when combined together will make up the full web application.

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

### Migration
- migration allows us to move databases from one design to another, this is also reversible.
- So we can migrate our databse

