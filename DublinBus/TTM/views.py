from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

from .scripts import predictions, userpredictions
from .models import Routes


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

def weather(request):
    return render(request)

def indexes(request):
    return render(request)

def map(request):
    return render(request, 'TTM/map.html')

def icon_circle(request):
    return render(request)

def icon_rec(request):
    return render(request)

def pickle(request):
    return render(request)

@csrf_exempt
def timepredict(request):
    request_data = request.COOKIES
    est_time = predictions(request_data)
    return render(request, 'TTM/est_time.html', {'est_time': est_time})

@csrf_exempt
def userpredictions(request):
    request_data = request.COOKIES
    est_time = userpredictions(request_data)
    return render(request, 'TTM/frequentuser.html', {'est_time': est_time})

def weather(request):
    return render(request)

def error_404(request):
    return render(request, 'TTM/error_404.html')

def error_500(request):
    return render(request, 'TTM/error_500.html')

def AAtweets(request):
    return render(request)

def DBtweets(request):
    return render(request)

def userlogin(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'TTM/login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('loggedin')
    else:
        return HttpResponseRedirect('invalid')

def loggedin(request):
    # reading a form to populate the database with additional user input.
    # u = FaveForm(request.POST)
    # if u.is_valid():
    #     u.save()
    # return render(request, 'TTM/loggedin.html', {'name': request.user.username, 'favourites': u })
    return render(request, 'TTM/loggedin.html', {'name': request.user.username})

def invalid(request):
    return render(request, 'TTM/invalid.html')

def logout(request):
    auth.logout(request)
    return render(request, 'TTM/login.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('loggedin')
    else:
        form = UserCreationForm()
    return render(request, 'TTM/signup.html', {'form': form})


