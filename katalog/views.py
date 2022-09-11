from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_item_katalog = CatalogItem.objects.all()
    context = {
        'data_item_katalog': data_item_katalog,
        'nama': 'Fadhlan Hasyim',
        'id': '2106652215',
    }
    return render(request, 'katalog.html', context)
