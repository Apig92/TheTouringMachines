from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from models import Routes
import json

def jsonfiles(request):
    f_json = open('routes.json', 'r')
    js_data = json.dumps(f_json)
    return render(request, 'ttm/index.html', {"my_data": js_data, })

def index(request):
    all_routes = Routes.objects.all()
    context = {'all_routes': all_routes, }
    return render(request, 'ttm/index.html', context)

def detail(request, Route_ID):
    try:
        route = Routes.objects.get(pk=Route_ID)
    except Routes.DoesNotExist:
        raise Http404("Route does not exist")
    return render(request, 'ttm/detail.html', {'route': route})
