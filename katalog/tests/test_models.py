from django.test import TestCase
from katalog.models import CatalogItem

class TestModels(TestCase):

    def setUp(self):
        self.catalog = CatalogItem.objects.create(
            item_name = 'Data Pribadi Joni',
            item_price = 123456,
            item_stock = 1,
            description = 'Informasi pribadi Yang Terhormat Bapak Joni',
            rating = 10,
            item_url = 'https://www.republika.co.id/berita/rhzlb1459/hacker-bjorka-bocorkan-data-pribadi-menkominfo-johnny-g-plate'
        )
    
    def test_create_catalog_item(self):
        self.assertEqual(
            self.catalog, 
            CatalogItem.objects.get(item_name = 'Data Pribadi Joni')
        )