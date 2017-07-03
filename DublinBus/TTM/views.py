from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Routes

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
