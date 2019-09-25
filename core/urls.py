from django.urls import path
from . import views
from django.conf.urls import url, include

urlpatterns = [
    path('', views.main, name='main'),
    path('ordered', views.ordered, name='ordered'),
    path('tip', views.tip, name='tip'),
    path('thrust', views.thrust, name='thrust'),
    path('steel_wheel', views.steel_wheel, name='steel_wheel'),
    path('anthers', views.anthers, name='anthers'),
    path('bearing', views.bearing, name='bearing'),
    path('brakepads', views.brakepads, name='brakepads'),
    path('filter', views.filter, name='filter'),
]