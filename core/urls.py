from django.urls import path, include

#import views
from . import views

#Configurar URLs
urlpatterns = [
    path('', views.index, name='index'),
]