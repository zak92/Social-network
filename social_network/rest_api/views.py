from snapp.models import *
from .serializers import *

# refactoring
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import viewsets


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsernameSerializer


class User(mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          generics.GenericAPIView):

  # field that is used to perform object lookup of individual model instances
  lookup_field = 'username'
  # select the appropriate queryset and  serializer
  queryset = User.objects.all()
  serializer_class = UserSerializer
  
  # This function displays the data to the user in the browsable API interface
  def get(self, request, *args, **kwargs):
      return self.retrieve(request, *args, **kwargs)

class AppUser(mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          generics.GenericAPIView):

  # field that is used to perform object lookup of individual model instances
  lookup_field = 'id'
  # select the appropriate queryset and  serializer
  queryset = AppUser.objects.all()
  serializer_class = AppUserSerializer
  
  # This function displays the data to the user in the browsable API interface
  def get(self, request, *args, **kwargs):
      return self.retrieve(request, *args, **kwargs)


class GroupDetail(mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          generics.GenericAPIView):

  # field that is used to perform object lookup of individual model instances
  lookup_field = 'name'
  # select the appropriate queryset and  serializer
  queryset = Group.objects.all()
  serializer_class = GroupDetailSerializer
  
  # This function displays the data to the user in the browsable API interface
  def get(self, request, *args, **kwargs):
      return self.retrieve(request, *args, **kwargs)
  
class GroupList(generics.ListAPIView):
  # select the appropriate queryset and  serializer
  queryset = Group.objects.all()
  serializer_class = GroupListSerializer
  
