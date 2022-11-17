
from django.urls import path

from route.views import showroute,showmap

urlpatterns = [
    path('<str:lat1>,<str:long1>,<str:lat2>,<str:long2>', showroute, name='showroute'),
    path('', showmap, name='showmap'),
    ]
