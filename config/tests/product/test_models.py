import pytest

# this is for allowing pytest to have access to the database
pytestmark = pytest.mark.django_db

from django.core.exceptions import ValidationError


class TestCategoryModels:
    def test_str_method(self, category_factory):
        # Arrange
        # Act
        x = category_factory(name="test_cat")
        # Assert
        assert x.__str__() == "test_cat"


class TestBrandModels:
    def test_str_method(self, brand_factory):
        # Arrange
        # Act
        x = brand_factory(name="test_cat")
        # Assert
        assert x.__str__() == "test_cat"


class TestProductModels:
    def test_str_method(self, product_factory):
        # Arrange
        # Act
        x = product_factory(name="test_cat")
        # Assert
        assert x.__str__() == "test_cat"


class TestProductLineModel:
    def test_str_model(self, product_line_factory):
        obj = product_line_factory(sku="1234")
        assert obj.__str__() == "1234"

    def test_duplicate_order_values(self, product_line_factory, product_factory):
        obj = product_factory()
        product_line_factory(order=1, product=obj)
        with pytest.raises(ValidationError):
            product_line_factory(order=1, product=obj).clean()


class TestProductImageModel:
    def test_str_method(self, product_image_factory):
        obj = product_image_factory(order=1)
        assert obj.__str__() == "1"
