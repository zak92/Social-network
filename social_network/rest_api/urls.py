from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='all-users'),
    path('user/<str:username>/', views.User.as_view(), name='user'),
    path('groups/', views.GroupList.as_view(), name='groups'), 
    path('group/<str:name>/', views.GroupDetail.as_view(), name='group-data'), 
   
   
   
]