from django.test import TestCase
import json
from django.urls import reverse
from django.urls import reverse_lazy
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from ..model_factories import *
from ...serializers import AppUserSerializer

class UserTest(APITestCase):
  appuser1 = None
  AppUserSerializer = None
  
  def setUp(self):
    # populate test database with dummy data from model_factories.py - AppUserFactory
    self.appuser1 = AppUserFactory()
    self.AppUserSerializer = AppUserSerializer(instance=self.appuser1)
   
  def tearDown(self):
    AppUser.objects.all().delete()
    AppUserFactory.reset_sequence(0)
   
  # check if all the necessary fields are there
  def test_AppUserSerializerCorrectFields(self):
    data = self.AppUserSerializer.data
    self.assertEqual(set(data.keys()), set( ['bio', 'status', 'profile_picture']))
  

  #check if all the the fields contain correct values
  def test_AppUserSerializerFieldData(self):
    data = self.AppUserSerializer.data
    # check if data is correct
    self.assertEqual(data['bio'], 'I am a superuser!')
    self.assertEqual(data['status'], 'In a meeting')
    self.assertEqual(data['profile_picture'], '/images/http%3A/127.0.0.1%3A8080/images/user.png')
    
   
    
