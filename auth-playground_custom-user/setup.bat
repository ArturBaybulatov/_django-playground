@echo off

call "venv.bat" &&^
python manage.py makemigrations base &&^
python manage.py migrate &&^
echo. &&^
echo === Creating an "admin" superuser. Enter information below === &&^
python manage.py createsuperuser --email=admin@example.com

pause
