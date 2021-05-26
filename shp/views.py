from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import ShpNepal

# Create your views here.
def shp(request):
    shpData  = serialize('geojson',ShpNepal.objects.all())
    return HttpResponse(shpData, content_type = 'geojson')

def index(request):
    return render(request,'shp/index.html')