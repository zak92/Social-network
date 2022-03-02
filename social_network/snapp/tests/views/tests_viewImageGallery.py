from django.test import TestCase
from django.urls import reverse
import json
from django.contrib.auth.models import AnonymousUser, User
from ...views import * 
from ...models import * 


class ViewImageGalleryViewTest(TestCase):
  user = None
  good_url = ''
  bad_url = ''

  def setUp(self):
    self.user = User.objects.create_user(username='test', password='12test12', email='test@example.com')
    self.user.save()
    self.good_url = reverse('viewImageGallery', kwargs={'pk': 'test'})
    self.bad_url = 'view-image-gallery/x/'
    
  def test_URLExists(self):
    response = self.client.get("/view-image-gallery/test/")
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
      self.assertTemplateUsed(response, 'snapp/image_gallery.html')