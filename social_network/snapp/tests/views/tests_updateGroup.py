from django.test import RequestFactory, TestCase
from django.urls import reverse
import json
from django.contrib.auth.models import AnonymousUser, User
from ...views import * 
from ...models import * 


class UpdateGroupViewTest(TestCase):
  user = None
  group = None
  good_url = ''
  bad_url = ''

  def setUp(self):
    self.factory = RequestFactory()
    self.user = User.objects.create_user(username='test', password='12test12', email='test@example.com')
    self.user.save()
    self.group = Group.objects.create(id=2, groupCreator=self.user, name='Test Group 2')
    self.group.save()
    self.good_url = reverse('updateGroup', kwargs={'pk': 2})
    self.bad_url = 'update-group/12/'

  def tearDown(self):
    self.user.delete()
    self.group.delete()
    
  def test_URLExists(self):
    request = self.factory.get("/update-group/2/")
    request.user = self.user
    response = updateGroup(request, pk=2)
    self.assertEqual(response.status_code, 200)

  def test_URLAccessibleByName(self):
    request = self.factory.get(self.good_url)
    request.user = self.user
    response = updateGroup(request, pk=2)
    self.assertEqual(response.status_code, 200)
    
  def test_FailOnBadURL(self):
    response = self.client.get(self.bad_url, format='json')
    self.assertEqual(response.status_code, 404)

  def test_UsesCorrectTemplate(self):
    self.client.login(username='test', password='12test12')
    response = self.client.get(self.good_url, format='json')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'snapp/group_form.html')