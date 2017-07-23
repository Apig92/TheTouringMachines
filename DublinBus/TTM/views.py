from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Routes
import json

def index(request):
    all_routes = Routes.objects.all()
    context = {'all_routes': all_routes,}
    return render(request, 'ttm/index.html', context)

def detail(request, Route_ID):
    try:
        route = Routes.objects.get(pk=Route_ID)
    except Routes.DoesNotExist:
        raise Http404("Route does not exist")
    return render(request, 'ttm/detail.html', {'route': route})

def json_routes(request):
    #json_data = json.dumps('TTM/static/TTM/JSON/routes.json')
    return render(request, 'ttm/json_routes.html')

def json_jpid(request, jpid):
    #json_jpid = json.dumps('TTM/static/TTM/JSON/' + jpid + '.json')
    return render(request, 'ttm/json_jpid.html')

def map(request):
    return render(request, 'ttm/map.html')

def icon_circle(request):
    return render(request)

def icon_rec(request):
    return render(request)
