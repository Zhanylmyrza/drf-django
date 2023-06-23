#Packages

django
python-dotenv 0.21.0
djangorestframework==3.14.0
pytest==7.3.2
pytest-django-4.5.2

django-mptt
drf-spectacular
coverage
pytest-cov

pytest-factoryboy


#Commands

django-admin startproject drfcommerce
./manage.py runserver
from django.core.management.utils import get_random_sercret_key
print(get_random_sercret_key())

python manage.py spectacular --file schema.yml
coverage run -m pytest
pytest --cov