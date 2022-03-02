from django.test import RequestFactory, TestCase
from django.urls import reverse
import json
from django.contrib.auth.models import AnonymousUser, User
from ...views import * 
from ...models import * 


class ImageGalleryViewTest(TestCase):
  user = None
  gallery = None
  good_url = ''
  bad_url = ''

  def setUp(self):
    self.factory = RequestFactory()
    self.user = User.objects.create_user(username='test', password='12test12', email='test@example.com')
    self.user.save()
    self.gallery = GalleryImage.objects.create(owner=self.user, image='cat.png')
    self.gallery.save()
    self.good_url = reverse('imageGallery')
    self.bad_url = 'image-gallery/'

  def tearDown(self):
    self.user.delete()
    self.gallery.delete()
    
  def test_URLExists(self):
    request = self.factory.get("/image-gallery")
    request.user = self.user
    response = imageGallery(request)
    self.assertEqual(response.status_code, 200)

  def test_URLAccessibleByName(self):
    request = self.factory.get(self.good_url)
    request.user = self.user
    response = imageGallery(request)
    self.assertEqual(response.status_code, 200)
    
  def test_FailOnBadURL(self):
    response = self.client.get(self.bad_url, format='json')
    self.assertEqual(response.status_code, 404)

  def test_UsesCorrectTemplate(self):
    self.client.login(username='test', password='12test12')
    response = self.client.get(self.good_url, format='json')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'snapp/image_gallery.html')