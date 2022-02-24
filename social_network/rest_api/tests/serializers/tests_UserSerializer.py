from django.test import TestCase
import json
from django.urls import reverse
from rest_framework.test import APITestCase
from ..model_factories import *
from ...serializers import *

class UserTest(APITestCase):
  user1 = None
  UserSerializer = None
 
  def setUp(self):
    # populate test database with dummy data from model_factories.py - UserFactory
    self.user1 = UserFactory()
    self.UserSerializer = UserSerializer(instance=self.user1)
  
  def tearDown(self):
    User.objects.all().delete()
    UserFactory.reset_sequence(0)
   

  # check if all the necessary fields are there
  def test_UserSerializerCorrectFields(self):
    data = self.UserSerializer.data
    self.assertEqual(set(data.keys()), set(['id', 'username', 'email', 'last_login', 'date_joined', 'appuser', 'gallery', 'contacts']))
  

  #check if all the the fields contain correct values
  def test_UserSerializerFieldData(self):
    data = self.UserSerializer.data
    # check if data is correct
    self.assertEqual(data['username'], 'admin')
    self.assertEqual(data['email'], 'admin@gmail.com')
    self.assertEqual(data['last_login'], '2022-02-23T21:00:53.896105Z')
    self.assertEqual(data['date_joined'], '2022-02-14T17:37:48.545521Z')
  
   

   
    
