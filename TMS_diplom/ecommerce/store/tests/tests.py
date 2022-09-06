from django.contrib.auth.models import User
from django.test import TestCase
from django.http import HttpRequest
from store.models import Category, Product
from store.views import *

from django.test import Client, RequestFactory


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        User.objects.create(username='admin123')
        Category.objects.create(name='Телефоны', slug='Телефоны')
        Product.objects.create(category_id=1, slug='Apple Iphone 12 Pro', name='Apple Iphone 12 Pro')

    def test_url_allowed_hosts(self):
        response = self.c.get('')
        self.assertEqual(response.status_code, 200)

    def test_category_url(self):
        response = self.c.get('collections')
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        request = HttpRequest()
        response = collections(request)
        self.assertEqual(response.status_code, 200)

    def test_view_function(self):
        request = self.factory.get('/collections/%D0%9D%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA%D0%B8/%D0%9D%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA%20Apple%20MacBook%20Pro%2016%22%202019%20MVVJ2')
        response = productview(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Home</html>', html)
        self.assertTrue()