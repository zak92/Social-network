
from django.urls import path
from . import views

urlpatterns = [
   
    path('login', views.userLogin, name="login"),
    path('logout', views.userLogout, name="logout"),
    path('sign-up', views.userSignUp, name="signUp"),
    path('home', views.home, name="home"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('group/<str:pk>/', views.group, name="group"),
    path('create-group', views.createGroup, name="createGroup"),
    path('update-group/<str:pk>/', views.updateGroup, name="updateGroup"),
    path('delete-group/<str:pk>/', views.deleteGroup, name="deleteGroup"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="deleteMessage"),
    path('update-profile', views.updateProfile, name="updateProfile"), 
    path('image-gallery', views.imageGallery, name="imageGallery"),
    path('view-image-gallery/<str:pk>/', views.viewImageGallery, name="viewImageGallery")   
]