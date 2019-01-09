## Setup

```
python manage.py makemigrations base
python manage.py migrate
python manage.py shell --command "from django.contrib.auth import get_user_model; get_user_model().objects.create_superuser('admin', 'admin@example.com', '123456')"
```

Generate some data:

```
python manage.py 01_generate_users
python manage.py 02_generate_categories
python manage.py 03_generate_notes
```
