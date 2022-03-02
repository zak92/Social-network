from django.test import RequestFactory, TestCase
from django.urls import reverse
import json
from django.contrib.auth.models import AnonymousUser, User
from ...views import * 
from ...models import * 


class UpdateProfileViewTest(TestCase):
  user = None
  appuser = None
  good_url = ''
  bad_url = ''

  def setUp(self):
    self.factory = RequestFactory()
    self.user = User.objects.create_user(username='test', password='12test12', email='test@example.com')
    self.appuser = AppUser.objects.create(user=self.user)
    self.user.save()
    self.appuser.save()
    self.good_url = reverse('updateProfile')
    self.bad_url = 'update-profile/'
  
  def tearDown(self):
    self.user.delete()
    self.appuser.delete()

# the requested user must be authenticated to access this page
  def test_URLExists(self):
    request = self.factory.get("/update-profile")
    request.user = self.user
    response = updateProfile(request)
    self.assertEqual(response.status_code, 200)

  def test_URLAccessibleByName(self):
    request = self.factory.get(self.good_url)
    request.user = self.user
    response = updateProfile(request)
    self.assertEqual(response.status_code, 200)

    
  def test_FailOnBadURL(self):
    response = self.client.get(self.bad_url, format='json')
    self.assertEqual(response.status_code, 404)

  def test_UsesCorrectTemplate(self):
    self.client.login(username='test', password='12test12')
    response = self.client.get(self.good_url, format='json')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'snapp/user_profile_settings.html')