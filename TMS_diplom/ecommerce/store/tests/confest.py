import pytest
from pytest_factoryboy import register
from django.urls import reverse
from store.tests.factories import CategoryFactory

register(CategoryFactory)

@pytest.fixture
def product_category(db, category_factory):
    category = category_factory.create()
    return category
