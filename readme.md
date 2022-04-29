# Crud Djando System 

## This a system crud the books
## Clone project 
```bash
git clone https://github.com/vinny523/Django_crud.git
```
## 🧞 Commands 

All commands are run from the root of the project, from a terminal: 


| Command           | Action                                       |
|:----------------  |:-------------------------------------------- |
| `python -m create venv venv`     | Create virtual venv                       |
| `python -m pip -r requeriments.txt`     | Install dependencies  |
| `python manage.py runserver`   | Starts local project server at `localhost:8000`    |


# Recommended configuration for the database

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bookshop',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
