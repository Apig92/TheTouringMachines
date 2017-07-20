from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^index$', views.index, name='index'),

    # /ttm/312/
    url(r'^(?P<Route_ID>[0-9]+)/$', views.detail, name='detail'),

    # /ttm/JSON/fsad.json
    url(r'^JSON/routes.json/$', views.json_routes, name='json_routes'),
    #url(r'^JSON/(\d||\w)*.json/$', views.json_routes, name='json_routes'),

    # /ttm/map.html
    #url(r'^(map.html)$', views.map, name='map'),
]
