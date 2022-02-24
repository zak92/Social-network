from django.test import TestCase
import json
from django.urls import reverse
from rest_framework.test import APITestCase
from ..model_factories import *
from ...serializers import GroupListSerializer


class GroupListTest(APITestCase):
  name1 = None
  GroupListSerializer = None
 
  def setUp(self):
    # populate test database with dummy data from model_factories.py - GroupFactory
    self.name1 = GroupFactory()
    self.GroupListSerializer = GroupListSerializer(instance=self.name1)
  
  def tearDown(self):
    Group.objects.all().delete()
    GroupFactory.reset_sequence(0)
   

  #check if all the necessary fields are there
  def test_GroupListSerializerCorrectFields(self):
    data = self.GroupListSerializer.data
    self.assertEqual(set(data.keys()), set(['name']))
  

  #check if all the the fields contain correct values
  def test_GroupListSerializerFieldData(self):
    data = self.GroupListSerializer.data
    # check if data is correct
    self.assertEqual(data['name'], 'Test')