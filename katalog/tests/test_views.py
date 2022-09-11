from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.katalog_url = reverse('katalog:katalog')

    def test_show_catalog_resolves(self):
        response = self.client.get(self.katalog_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'katalog.html')