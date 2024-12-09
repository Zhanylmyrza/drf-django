import factory

from drfecommerce.product.models import Brand, Category, Product

class CategoryFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = Category
    
  name="test_category"