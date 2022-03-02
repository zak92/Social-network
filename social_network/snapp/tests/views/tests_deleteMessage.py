from django.test import RequestFactory, TestCase
from django.urls import reverse
import json
from django.contrib.auth.models import AnonymousUser, User
from ...views import * 
from ...models import * 


class DeleteMessageViewTest(TestCase):
  user = None
  group = None
  message = None
  good_url = ''
  bad_url = ''

  def setUp(self):
    self.factory = RequestFactory()
    self.user = User.objects.create_user(username='test', password='12test12', email='test@example.com')
    self.user.save()
    self.group = Group.objects.create(id=2, groupCreator=self.user, name='Test Group 2')
    self.group.save()
    self.message = Message.objects.create(id=2, user=self.user, group=self.group, message="Delete this message")
    self.good_url = reverse('deleteMessage', kwargs={'pk': 2})
    self.bad_url = 'delete-message/100/'

  def tearDown(self):
    self.user.delete()
    self.group.delete()
    self.message.delete()
    
  def test_URLExists(self):
    request = self.factory.get("/delete-message/2/")
    request.user = self.user
    response = deleteMessage(request, pk=2)
    self.assertEqual(response.status_code, 200)

  def test_URLAccessibleByName(self):
    request = self.factory.get(self.good_url)
    request.user = self.user
    response = deleteGroup(request, pk=2)
    self.assertEqual(response.status_code, 200)
    
  def test_FailOnBadURL(self):
    response = self.client.get(self.bad_url, format='json')
    self.assertEqual(response.status_code, 404)

  def test_UsesCorrectTemplate(self):
    self.client.login(username='test', password='12test12')
    response = self.client.get(self.good_url, format='json')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'snapp/delete.html')