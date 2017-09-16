# best-blog-in-the-world

Django Girls blog

## Installation

- Create virtualenv. Either `virtualenv virtual && source virtual/bin/activate` or `mkvirtualenv blog && workon blog`
- Install Django `pip install Django`
- Freeze requirements `pip freeze > requirements.txt`
- Note: Next time install project with `pip install -r requirements.txt`

## Install Docker

- For Windows: `https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe`
- For Mac: `https://download.docker.com/mac/stable/Docker.dmg`
- Run Docker service in background

## Setup database

- Create database service `docker-compose up`
- After first boot database service will require restart
- Restart database service with `Ctrl+C` and run again `docker-compose up`
- Do not close database service terminal window
- Change database config in `settings.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'localhost',
        'PORT': 5433,
    }
}
```

## Configure project for new database

- Install PostgreSQL support library `pip install psycopg2` 
- Apply migrations `python manage.py migrate`
- Create superuser `python manage.py createsuperuser`

## Use DataGrip or PyCharm Professional Database view

- Configure new postgres connection under `localhost:5433`
- Use database `postgres` and login `postgres`
- View tables `auth_user`, `django_migrations` and `blog_post`

## Run

- Run server `python manage.py runserver`

## Start coding

- Create your own branch `git checkout -b $name`
- Use `django-admin startapp $name` or `python manage.py startapp $name` where `$name` is your name
- Add changes with `git add . && git commit -m "Your message here."` 
- Push it to GitHub `git push origin $name`

## Tasks

- Install `https://github.com/django-extensions/django-extensions`
- Install `https://github.com/bpython/bpython`
- Remember to freeze requirements `pip freeze > requirements.txt`
- Use `python manage.py shell_plus`
- Notice how models are automatically loaded and how autocomplete works
- Use `shell_plus` in future in favour of `shell`
- Add, commit and push changes to your branch on GitHub
- Make your first Pull Request on GitHub (your branch to master)

## Task ideas

- Django Girls extension (skip optional steps): `https://djangogirls.gitbooks.io/django-girls-tutorial-extensions`
- Do some agile stuff (daily, retro, brainstorming and planning)
- Conquer the moon!
