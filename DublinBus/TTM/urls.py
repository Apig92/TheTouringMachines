from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^index.html$', views.index, name='index'),

    # /TTM/312/
    url(r'^(?P<Route_ID>[0-9]+)/$', views.detail, name='detail'),

    # static/TTM/JSON/routes.json
    url(r'^static/TTM/JSON/routes.json/$', views.json_routes, name='json_route'),

    # /TTM/JSON/routeinfo.json
    url(r'^static/TTM/JSON/routeinfo.json/$', views.routeinfo, name='routeinfo'),

    # /TTM/map.html
    url(r'^map.html$', views.map, name='map'),

    # /TTM/static/TTM/Images/icon_circle.png
    url(r'^static/TTM/images/icon_circle.png$', views.icon_circle, name='icon_circle'),

    # /TTM/static/TTM/Images/icon_rec.png
    url(r'^static/TTM/images/icon_rec.png$', views.icon_rec, name='icon_rec'),
]
