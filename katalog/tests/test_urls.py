from re import S
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from katalog.views import show_katalog

class TestUrls(SimpleTestCase):

    def setUp(self):
        self.katalog_url = reverse('katalog:katalog')

    def test_katalog_url_resolves(self):
        self.assertEqual(resolve(self.katalog_url).func, show_katalog)
