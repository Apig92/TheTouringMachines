from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Routes
from .scripts import predictions
from .testing import testing
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    all_routes = Routes.objects.all()
    context = {'all_routes': all_routes,}
    return render(request, 'TTM/index.html', context)

def detail(request, Route_ID):
    try:
        route = Routes.objects.get(pk=Route_ID)
    except Routes.DoesNotExist:
        raise Http404("Route does not exist")
    return render(request, 'TTM/detail.html', {'route': route})

def json_routes(request):
    return render(request)

def routeinfo(request):
    return render(request)

def map(request):
    return render(request, 'TTM/map.html')

def icon_circle(request):
    return render(request)

def icon_rec(request):
    return render(request)

@csrf_exempt
def timepredict(request):
    request_data = request.COOKIES
    est_time = predictions(request_data)
    return render(request, 'TTM/est_time.html', {'est_time': est_time})


def test(request, x):
    print(testing(x))


def pickle(request):
    return render(request)
