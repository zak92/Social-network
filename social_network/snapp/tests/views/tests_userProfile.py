from django.test import TestCase
from django.urls import reverse
import json
from django.contrib.auth.models import AnonymousUser, User
from ...views import * 


class UserProfileTest(TestCase):
  user = None
  good_url = ''
  bad_url = ''

  def setUp(self):
    self.user = User.objects.create_user(id=1, username='test', password='12test12', email='test@example.com')
    self.user.save()
    self.good_url = reverse('user-profile', kwargs={'pk': 1})
    self.bad_url = '/user-profile/x'

  def tearDown(self):
    self.user.delete()
    
  def test_URLExists(self):
    response = self.client.get("/profile/1/")
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
    self.assertTemplateUsed(response, 'snapp/user_profile.html')