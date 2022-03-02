from django.test import TestCase
from django.urls import reverse
import json
from django.contrib.auth.models import AnonymousUser, User
from ...views import * 


class UserSignUpViewTest(TestCase):
  good_url = ''
  bad_url = ''

  def setUp(self):
    self.user = User.objects.create_user(username='test', password='12test12', email='test@example.com')
    self.good_url = reverse('signUp')
    self.bad_url = '/sign-up/'
    
  def tearDown(self):
      self.user.delete()

  def test_URLExists(self):
    response = self.client.get("/sign-up")
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

