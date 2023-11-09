from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('addPoints/', views.addPoints, name='addPoints'),
        path('reset/', views.reset, name='reset'),
        path('confirmPoints/', views.confirmPoints, name='confirmPoints'),
        path('confirmStudents/', views.confirmStudents, name='confirmStudents'),
        path('confirmAll/', views.confirmAll, name='confirmAll'),
]
