from django.test import TestCase
import json
from django.urls import reverse
from django.urls import reverse_lazy
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from ..model_factories import *
from ...serializers import *


class AppUserTest(APITestCase):
  user1 = None
  good_url = ''
  bad_url = ''
  
  def setUp(self):
    # populate test database with dummy data from model_factories.py - UserFactory
    self.user1 = AppUserFactory()
    self.good_url = reverse('user', kwargs={'username': 'admin'})
    self.bad_url = '/api/user/X/'
   
  def tearDown(self):
    User.objects.all().delete()
    UserFactory.reset_sequence(0)
    AppUser.objects.all().delete()
    AppUserFactory.reset_sequence(0)


   # test for successful response code for user endpoint
  def test_AppUserResponseSuccessCode(self):
    response = self.client.get(self.good_url, format='json')
    # access the response data
    response.render()
    # test if the http code is 200
    self.assertEqual(response.status_code, 200)

  # if user send wrong username - user must get 404 code
  def test_AppUserReturnFailOnBadUsername(self):
    response = self.client.get(self.bad_url, format='json')
    self.assertEqual(response.status_code, 404)

  # check if all the necessary fields are there
  def test_AppUserCorrectFields(self):
    response = self.client.get(self.good_url, format='json')
    response.render() 
    # check if data is correct
    data = json.loads(response.content)
    self.assertTrue('username' in data)
    self.assertTrue('email' in data)
    self.assertTrue('last_login' in data)
    self.assertTrue('date_joined' in data) 
    self.assertTrue('appuser' in data) 
    self.assertTrue('gallery' in data) 
    self.assertTrue('contacts' in data) 

  # check if all the the fields contain correct values
  def test_AppUserFieldData(self):
    response = self.client.get(self.good_url, format='json')
    response.render()
    # check if data is correct
    data = json.loads(response.content)
    self.assertEqual(data['username'], 'admin')
    self.assertEqual(data['email'], 'admin@gmail.com')
    self.assertEqual(data['last_login'], '2022-02-23T21:00:53.896105Z')
    self.assertEqual(data['date_joined'], '2022-02-14T17:37:48.545521Z')
    self.assertEqual(data['appuser'], { 'bio': 'I am a superuser!',
                                        'status': 'In a meeting',
                                        'profile_picture': 'http://testserver/images/http%3A/127.0.0.1%3A8080/images/user.png'
                                        })
   