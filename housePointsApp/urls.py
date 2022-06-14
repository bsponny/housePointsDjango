from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('addPoints/', views.addPoints, name='addPoints'),
        path('reset/', views.reset, name='reset'),
]
