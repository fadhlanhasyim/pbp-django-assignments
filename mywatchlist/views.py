from django.shortcuts import render
from mywatchlist.models import MywatchlistModel
from django.core import serializers
from django.http import HttpResponse

# Create your views here.
def show_mywatchlist(request):
    data_mywatchlist = MywatchlistModel.objects.all()
    total_watched = MywatchlistModel.objects.filter(watched=True).count()
    total_unwatched = MywatchlistModel.objects.filter(watched=False).count()
    if total_watched >= total_unwatched:
        text = "Selamat, kamu sudah banyak menonton!"
    else:
        text = "Wah, kamu masih sedikit menonton!"
    context = {
        "data_mywatchlist":data_mywatchlist,
        "nama":"Fadhlan Hasyim",
        "npm":"2106652215",
        "text":text
    }
    return render(request, 'mywatchlist.html', context)

def show_mywatchlist_xml(request):
    data_mywatchlist = MywatchlistModel.objects.all()
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")

def show_mywatchlist_xml_by_id(request, id):
    data_mywatchlist = MywatchlistModel.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")

def show_mywatchlist_json(request):
    data_mywatchlist = MywatchlistModel.objects.all()
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")

def show_mywatchlist_json_by_id(request, id):
    data_mywatchlist = MywatchlistModel.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")