from django.test import TestCase
from django.urls import reverse
import json
from django.contrib.auth.models import AnonymousUser, User
from ...views import * 


class UserLoginViewTest(TestCase):
  good_url = ''
  bad_url = ''

  def setUp(self):
    self.user = User.objects.create_user(username='test', password='12test12', email='test@example.com')
    self.user.save()
    self.good_url = reverse('login')
    self.bad_url = '/logins/'

  def tearDown(self):
    self.user.delete()
    
  def test_URLExists(self):
    response = self.client.get("/login")
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
    self.assertTemplateUsed(response, 'snapp/index.html')

  # test if a user is authenticated - correct password and username
  def test_UserAuthenticated(self):
      user = authenticate(username='test', password='12test12')
      self.assertTrue((user is not None) and user.is_authenticated)

  # user not authenticated on wrong username
  def test_WrongUsername(self):
      user = authenticate(username='wrong', password='12test12')
      self.assertFalse(user is not None and user.is_authenticated)

 # user not authenticated on wrong password
  def test_WrongPassword(self):
      user = authenticate(username='test', password='wrong')
      self.assertFalse(user is not None and user.is_authenticated)