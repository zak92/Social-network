from django.test import TestCase
import json
from django.urls import reverse
from django.urls import reverse_lazy
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from ..model_factories import *
from ...serializers import *


class GroupTest(APITestCase):
  group1 = None
  good_url = ''
  bad_url = ''
  
  def setUp(self):
    # populate test database with dummy data from model_factories.py - UserFactory
    self.group1 = GroupFactory()
    self.good_url = reverse('group_data', kwargs={'name': 'Test'})
    self.bad_url = '/api/group/X/'
   
  def tearDown(self):
    User.objects.all().delete()
    UserFactory.reset_sequence(0)
    Group.objects.all().delete()
    GroupFactory.reset_sequence(0)


   # test for successful response code for user endpoint
  def test_GroupResponseSuccessCode(self):
    response = self.client.get(self.good_url, format='json')
    # access the response data
    response.render()
    # test if the http code is 200
    self.assertEqual(response.status_code, 200)

  # if user send wrong username - user must get 404 code
  def test_GroupReturnFailOnBadUsername(self):
    response = self.client.get(self.bad_url, format='json')
    self.assertEqual(response.status_code, 404)

  # check if all the necessary fields are there
  def test_GroupCorrectFields(self):
    response = self.client.get(self.good_url, format='json')
    response.render() 
    # check if data is correct
    data = json.loads(response.content)
    self.assertTrue('groupCreator' in data)
    self.assertTrue('name' in data)
    self.assertTrue('id' in data)
    self.assertTrue('description' in data)
    self.assertTrue('lastUpdated' in data)
    self.assertTrue('dateCreated' in data) 
    self.assertTrue('members' in data) 
    
  

  # check if all the the fields contain correct values
  def test_GroupFieldData(self):
    response = self.client.get(self.good_url, format='json')
    response.render()
    # check if data is correct
    data = json.loads(response.content)
    self.assertEqual(data['id'], 1)
    self.assertEqual(data['name'], 'Test')
    self.assertEqual(data['description'], 'This is a Test Group')
    self.assertEqual(data['lastUpdated'], data['lastUpdated'])
    self.assertEqual(data['dateCreated'], data['dateCreated'])
    self.assertEqual(data['groupCreator'], {'username': 'admin'})
    self.assertEqual(data['members'], [])

   