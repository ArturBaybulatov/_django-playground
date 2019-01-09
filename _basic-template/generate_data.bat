@echo off

call "venv.bat" &&^
python manage.py 01_generate_brands &&^
python manage.py 02_generate_categories &&^
python manage.py 03_generate_products

pause
