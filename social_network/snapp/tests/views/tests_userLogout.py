from django.test import TestCase
from django.urls import reverse
import json
from django.contrib.auth.models import AnonymousUser, User
from ...views import * 


class UserLogoutViewTest(TestCase):
  good_url = ''
  bad_url = ''

  def setUp(self):
    self.good_url = reverse('home')
    self.bad_url = '/login/'
  
  # when user log out, user is redirected to home page
  def test_URLExists(self):
    response = self.client.get("/home")
    self.assertEqual(response.status_code, 200)

  def test_URLAccessibleByName(self):
    response = self.client.get(self.good_url, format='json')
    self.assertEqual(response.status_code, 200)
    
  def test_FailOnBadURL(self):
    response = self.client.get(self.bad_url, format='json')
    self.assertEqual(response.status_code, 404)

  def test_UsesCorrectTemplate(self):
    response = self.client.get(self.good_url, format='json')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'snapp/home.html')