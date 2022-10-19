from django.contrib.auth.models import User
from django.test import TestCase
from store.models import Category, Product

from django.test import Client

class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()

        def test_url_allowed_host(self):
            response = self.c.get('')
            self.assertEqual(response.status_code, 200)

