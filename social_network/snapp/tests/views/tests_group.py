from django.test import TestCase
from django.urls import reverse
import json
from django.contrib.auth.models import AnonymousUser, User
from ...views import * 
from ...models import * 


class GroupViewTest(TestCase):
  user = None
  group = None
  good_url = ''
  bad_url = ''

  def setUp(self):
    self.user = User.objects.create_user(username='test', password='12test12', email='test@example.com')
    self.user.save()
    self.group = Group.objects.create(id=1, groupCreator=self.user, name='Test Group')
    self.group.save()
    self.good_url = reverse('group', kwargs={'pk': 1})
    self.bad_url = 'groups/12/'

  def tearDown(self):
    self.user.delete()
    self.group.delete()
    
  def test_URLExists(self):
    response = self.client.get("/group/1/")
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
    self.assertTemplateUsed(response, 'snapp/group.html')