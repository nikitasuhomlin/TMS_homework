import factory
from store.models import Category
from faker import Faker

fake = Faker()

### Catalogue ###


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "Телефоны"
    slug = "Телефоны"