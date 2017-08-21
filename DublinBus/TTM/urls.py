from django.conf.urls import url
from . import views

urlpatterns = [


    url(r'^login$', views.userlogin, name = 'login'),
    url(r'^auth$', views.auth_view, name = 'auth'),
    url(r'^loggedout$', views.logout, name = 'logout'),
    url(r'^loggedin$', views.loggedin, name = 'loggedin'),
    url(r'^invalid$', views.invalid, name = 'invalid'),
    url(r'^signup.html$', views.signup, name='signup'),


    # /TTM/index.html
    url(r'^index.html$', views.index, name='index'),

    # static/TTM/JSON/routes.json
    url(r'^static/TTM/JSON/routes.json$', views.json_routes, name='json_route'),

    # /TTM/JSON/routeinfo.json
    url(r'^static/TTM/JSON/routeinfo.json$', views.routeinfo, name='routeinfo'),

    # /TTM/map.html
    url(r'^map.html$', views.map, name='map'),

    # /TTM/static/TTM/Images/icon_circle.png
    url(r'^static/TTM/images/icon_circle.png$', views.icon_circle, name='icon_circle'),

    # /TTM/static/TTM/Images/icon_rec.png
    url(r'^static/TTM/images/icon_rec.png$', views.icon_rec, name='icon_rec'),

    # /TTM/detail.html
    url(r'^detail.html$', views.detail, name='detail'),

    # /TTM/est_time.html
    url(r'^est_time.html$', views.timepredict, name='est_time'),

    # static/TTM/pickles/line.sav
    url(r'^static/TTM/pickles/[\d]*[\w]*CLEANrouteweather.sav$', views.pickle, name='pickle'),

    # /TTM/JSON/weather.json
    url(r'^static/TTM/JSON/weather.json$', views.weather, name='weather'),

    # /TTM/error_404
    url(r'^error_404$', views.error_404, name='error_404'),

# static/TTM/JSON/routes.json
    url(r'^static/TTM/JSON/indexes.json$', views.indexes, name='indexes'),


    # /TTM/error_500
    url(r'^error_500$', views.error_500, name='error_500'),

    # /TTM/JSON/AAtweets.json
    url(r'^static/TTM/JSON/AAtweets.json$', views.AAtweets, name='AAtweets'),
]
