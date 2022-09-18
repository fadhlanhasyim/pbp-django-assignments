from unicodedata import name
from django.urls import path
from mywatchlist.views import show_mywatchlist, show_mywatchlist_json, show_mywatchlist_xml, show_mywatchlist_json_by_id, show_mywatchlist_xml_by_id

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('html/', show_mywatchlist, name='show_mywatchlist'),
    path('json/', show_mywatchlist_json, name='show_mywatchlist_json'),
    path('xml/', show_mywatchlist_xml, name='show_mywatchlist_xml'),
    path('json/<int:id>/', show_mywatchlist_json_by_id, name='show_mywatchlist_json_by_id'),
    path('xml/<int:id>/', show_mywatchlist_xml_by_id, name='show_mywatchlist_xml_by_id'),
]