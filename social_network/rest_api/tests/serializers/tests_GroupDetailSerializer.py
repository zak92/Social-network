from django.test import TestCase
import json
from django.urls import reverse
from rest_framework.test import APITestCase
from ..model_factories import *
from ...serializers import GroupDetailSerializer

class GroupDetailTest(APITestCase):
  group1 = None
  GroupDetailSerializer = None
 
  def setUp(self):
    # populate test database with dummy data from model_factories.py - UserFactory
    self.group1 = GroupFactory()
    self.GroupDetailSerializer = GroupDetailSerializer(instance=self.group1)
  
  def tearDown(self):
    Group.objects.all().delete()
    GroupFactory.reset_sequence(0)
   

  # check if all the necessary fields are there
  def test_GroupDetailSerializerCorrectFields(self):
    data = self.GroupDetailSerializer.data
    self.assertEqual(set(data.keys()), set(['id', 'name', 'description','lastUpdated', 'dateCreated', 'groupCreator', 'members']))
  

  #check if all the the fields contain correct values
  def test_GroupDetailSerializerFieldData(self):
    data = self. GroupDetailSerializer.data
    # check if data is correct
    self.assertEqual(data['id'], 1)
    self.assertEqual(data['name'], 'Test')
    self.assertEqual(data['description'], 'This is a Test Group')
    self.assertEqual(data['lastUpdated'], data['lastUpdated'])
    self.assertEqual(data['dateCreated'], data['dateCreated'])
    self.assertEqual(data['groupCreator'], {'username': 'admin'})
    self.assertEqual(data['members'], [])
  
   

   
    
