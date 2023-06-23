import pytest

pytestmark = pytest.mark.django_db

class TestCategoryModel:
  def test_str_method(self,category_factory):
    x=category_factory(name="test_cat")
    assert x.__str__() == "test_cat"

class TestBrandModel:
  def test_str_method(self, brand_factory):
    obj=brand_factory(name="test_brand")
    
    assert obj.__str__() == "test_brand"

class TestProductModel:
  pass
