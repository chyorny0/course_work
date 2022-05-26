from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('car', views.car, name='car'),
    path('restoration', views.restoration, name='restoration'),
    path('car_create', views.car_create, name='car_create'),
    path('car_ordered', views.car_ordered, name='car_ordered'),
    path('restoration_ordered', views.restoration_ordered, name='restoration_ordered'),
    path('car_filtrated', views.car_filtrated, name='car_filtrated'), 
    path('restoration_filtrated', views.restoration_filtrated, name='restoration_filtrated'), 
    path('range', views.range, name='range'),
    path('rangeresult', views.rangeresult, name='rangeresult'), 
]
