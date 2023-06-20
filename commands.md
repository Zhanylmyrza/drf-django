#Packages

django
python-dotenv 0.21.0
djangorestframework==3.14.0
pytest==7.3.2
pytest-django-4.5.2

#Commands

django-admin startproject drfcommerce
./manage.py runserver
from django.core.management.utils import get_random_sercret_key
print(get_random_sercret_key())