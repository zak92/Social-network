from django.test import TestCase
import json
from django.urls import reverse
from rest_framework.test import APITestCase
from ..model_factories import *
from ...serializers import UsernameSerializer

class UsernameTest(APITestCase):
  user1 = None
  UsernameSerializer = None
 
  def setUp(self):
    # populate test database with dummy data from model_factories.py - UserFactory
    self.user1 = UserFactory()
    self.UsernameSerializer = UsernameSerializer(instance=self.user1)
  
  def tearDown(self):
    User.objects.all().delete()
    UserFactory.reset_sequence(0)
   

  # check if all the necessary fields are there
  def test_UsernameSerializerCorrectFields(self):
    data = self.UsernameSerializer.data
    self.assertEqual(set(data.keys()), set(['username']))
  

  #check if all the the fields contain correct values
  def test_UsernameSerializerFieldData(self):
    data = self.UsernameSerializer.data
    # check if data is correct
    self.assertEqual(data['username'], 'admin')
   
   

   
    
