from django.urls import path
from . import views
from route.views import showroute, showmap

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:lat1>,<str:long1>,<str:lat2>,<str:long2>', showroute, name='showroute'),
    path('route/', showmap, name='showmap'),
    ]
