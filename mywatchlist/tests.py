from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.mywatchlist_html_url = reverse('mywatchlist:show_mywatchlist')
        self.mywatchlist_json_url = reverse('mywatchlist:show_mywatchlist_json')
        self.mywatchlist_xml_url = reverse('mywatchlist:show_mywatchlist_xml')

    def test_show_mywatchlist_html_resolves(self):
        response = self.client.get(self.mywatchlist_html_url)
        self.assertEqual(response.status_code, 200)

    def test_show_mywatchlist_json_resolves(self):
        response = self.client.get(self.mywatchlist_json_url)
        self.assertEqual(response.status_code, 200)

    def test_show_mywatchlist_xml_resolves(self):
        response = self.client.get(self.mywatchlist_xml_url)
        self.assertEqual(response.status_code, 200)