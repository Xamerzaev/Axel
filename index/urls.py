from django.urls import path
from . import views

from .views import Home
from route.views import showroute, showmap

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('<str:lat1>,<str:long1>,<str:lat2>,<str:long2>', showroute, name='showroute'),
    path('route/', showmap, name='showmap'),
    ]
