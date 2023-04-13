from django.urls import path, include

#import views
from . import views

#Configurar URLs
urlpatterns = [
    path('', views.posts, name='posts'),
    path('<int:id>/', views.post, name='post'),
]