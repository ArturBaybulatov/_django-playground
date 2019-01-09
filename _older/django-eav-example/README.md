### Setup

```
virtualenv .env --python python3.4 && \
source .env/bin/activate && \
pip install --requirement requirements.txt
```

then:

```
python manage.py runserver
```

or:

```
sudo $(which python) manage.py runserver 80
```

In case databases aren't present:

```
python manage.py makemigrations eav app && python manage.py migrate
```

and navigate to the `/setup/` URL

To start an interactive shell:

```
python manage.py shell_plus --use-pythonrc
```
