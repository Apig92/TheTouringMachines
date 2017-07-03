from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),

    # /ttm/312/
    url(r'^(?P<Route_ID>[0-9]+)/$', views.detail, name='detail'),
]
