import profile
import factory
from django.test import TestCase
from django.conf import settings
from django.core.files import File
from snapp.models import *

from random import randint
from random import choice

# TEST FIXTURES
class UserFactory(factory.django.DjangoModelFactory):
  id = 1
  username = 'admin'
  email = 'admin@gmail.com'
  last_login = '2022-02-23T21:00:53.896105Z'
  date_joined = '2022-02-14T17:37:48.545521Z'
  class Meta:
    model = User

class AppUserFactory(factory.django.DjangoModelFactory):
  user =  factory.SubFactory(UserFactory) 
  bio = 'I am a superuser!'
  status = 'In a meeting'
  profile_picture = 'http://127.0.0.1:8080/images/user.png'
 
  class Meta:
    model = AppUser
  

class GalleryImageFactory(factory.django.DjangoModelFactory):
  owner =  factory.SubFactory(UserFactory) 
  image = "http://127.0.0.1:8080/images/test_image_rvDQSv4_HTMwIRR.jpg"
      
  class Meta:
    model = GalleryImage


class GroupFactory(factory.django.DjangoModelFactory):
  groupCreator = factory.SubFactory(UserFactory) 
  id = 1
  name = 'Test'
  description = 'This is a Test Group'

  class Meta:
    model = Group


class AllUsersFactory(UserFactory):
  username = [
     {"username": "zak6566"},
     {"username": "zak92"}
  ]

class AllGroupsFactory(GroupFactory):
  name = [
     {"name": "testGroup1"},
     {"name": "testGroup2"}
  ]



 