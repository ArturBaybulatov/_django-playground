### Setup

```
virtualenv env --python python3.5 && \
source env/bin/activate && \
pip install --requirement requirements-dev.txt
```

Afterwards:

```
python manage.py makemigrations api && python manage.py migrate
```

then:

```
python manage.py runserver
```

and go to `/api/setup` or start up a shell:

```
python manage.py shell_plus --use-pythonrc
```

and do `models.setup()`
