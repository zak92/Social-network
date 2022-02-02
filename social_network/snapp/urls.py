
from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.index, name="index"),
    path('home', views.home, name="home"),
    path('userHome', views.userHome, name="userHome"),
    path('group/<str:pk>/', views.group, name="group"),
    path('create-group', views.createGroup, name="createGroup")
]