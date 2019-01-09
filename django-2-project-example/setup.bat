@echo off

call "venv.bat" &&^
python manage.py makemigrations base &&^
python manage.py migrate &&^
echo. &&^
echo Creating an "admin" superuser... &&^
python manage.py shell --command "from django.contrib.auth import get_user_model; get_user_model().objects.create_superuser('admin', 'admin@example.com', '123456')"

pause
