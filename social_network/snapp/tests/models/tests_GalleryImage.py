import profile
from django.test import RequestFactory, TestCase
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser, User
from ...models import GalleryImage

class GalleryImageModelTest(TestCase):

  user = None

  @classmethod
  def setUp(self):
    self.user = User.objects.create_user(username='test', password='12test12', email='test@example.com')
    GalleryImage.objects.create(
      id=1,
      owner = self.user, 
      image = 'cats.png'
    )

  def tearDown(self):
    User.objects.all().delete()
    GalleryImage.objects.all().delete()

   # check that the model has the correct field names
  def test_ModelHasCorrectFieldNames(self):
    gallery = GalleryImage.objects.get(id=1)
    field_label_owner = gallery._meta.get_field('owner').verbose_name
    field_label_image = gallery._meta.get_field('image').verbose_name
    self.assertEqual(field_label_owner, 'owner')
    self.assertEqual(field_label_image, 'image')
  
  #check that the model has correct field values
  def test_ModelHasCorrectFieldValues(self):
    gallery = GalleryImage.objects.get(id=1)
    self.assertEqual(gallery.owner.username, 'test')
    self.assertEqual(gallery.image, 'cats.png')
  
  #test model methods
  def test_ModelMethod(self):
    gallery = GalleryImage.objects.get(id=1)
    expected_object = gallery.owner.username
    self.assertEqual(expected_object, str(gallery.owner.username)) 