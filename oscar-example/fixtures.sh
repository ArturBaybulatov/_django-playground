source ../../_django-playground-venv/oscar-example/Scripts/activate

python manage.py loaddata fixtures/child_products.json &&
python manage.py oscar_import_catalogue fixtures/*.csv &&
python manage.py oscar_import_catalogue_images fixtures/images.tar.gz &&
python manage.py oscar_populate_countries --initial-only &&
python manage.py loaddata fixtures/pages.json fixtures/auth.json fixtures/ranges.json fixtures/offers.json &&
python manage.py loaddata fixtures/orders.json fixtures/promotions.json
