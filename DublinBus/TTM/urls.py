from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^index.html$', views.index, name='index'),

    # /ttm/312/
    url(r'^(?P<Route_ID>[0-9]+)/$', views.detail, name='detail'),

    # static/TTM/JSON/routes.json
    url(r'^static/TTM/JSON/routes.json/$', views.json_routes, name='json_route'),

    # /ttm/JSON/040D1001.json
    url(r'^static/TTM/JSON/([\d]*[\w]*).json/$', views.json_jpid, name='json_jpid')

    # /ttm/map.html
    #url(r'^(map.html)$', views.map, name='map'),
]
