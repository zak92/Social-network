from django.test import TestCase
import json
from django.urls import reverse
from django.urls import reverse_lazy
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from ..model_factories import *
from ...serializers import *


class AllGroupsTest(APITestCase):
  groups = None
  good_url = ''
  bad_url = ''
  
  def setUp(self):
    # populate test database with dummy data from model_factories.py - AllGroupsFactory
    self.groups = AllGroupsFactory()
    self.good_url = reverse('all_groups')
    self.bad_url = '/api/groupX/'
   
  def tearDown(self):
    Group.objects.all().delete()
    GroupFactory.reset_sequence(0)

   # test for successful response code for user endpoint
  def test_AllGroupsResponseSuccessCode(self):
    response = self.client.get(self.good_url, format='json')
    # access the response data
    response.render()
    # test if the http code is 200
    self.assertEqual(response.status_code, 200)

  #if user send wrong username - user must get 404 code
  def test_AllGroupsReturnFailOnBadURL(self):
    response = self.client.get(self.bad_url, format='json')
    self.assertEqual(response.status_code, 404)

  # check if a list is returned
  def test_AllGroupsCorrectFields(self):
    response = self.client.get(self.good_url, format='json')
    response.render() 
    # check if data is correct
    data = json.loads(response.content)
    self.assertIsInstance(data, list)
    self.assertIsInstance(data[0], dict)
    
  # check if all the the fields contain correct values
  def test_AllGroupsFieldData(self):
    response = self.client.get(self.good_url, format='json')
    response.render()
    # check if data is correct
    data = json.loads(response.content)
    self.assertEqual(data, [{'name': "[{'name': 'testGroup1'}, {'name': 'testGroup2'}]"}])
  
   
   