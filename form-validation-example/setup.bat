@echo off

call "venv.bat" &&^
python manage.py makemigrations base &&^
python manage.py migrate &&^
echo. &&^
echo === Creating a "admin" superuser. Enter information below === &&^
python manage.py createsuperuser --username=admin --email=admin@example.com &&^
python manage.py generate_records

pause
