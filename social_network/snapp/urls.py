
from django.urls import path
from . import views

urlpatterns = [
   
    path('login', views.userLogin, name="login"),
    path('logout', views.userLogout, name="logout"),
    path('sign-up', views.userSignUp, name="signUp"),
    path('home', views.home, name="home"),
    path('userHome', views.userHome, name="userHome"),
    path('group/<str:pk>/', views.group, name="group"),
    path('create-group', views.createGroup, name="createGroup"),
    path('update-group/<str:pk>/', views.updateGroup, name="updateGroup"),
    path('delete-group/<str:pk>/', views.deleteGroup, name="deleteGroup"),
]