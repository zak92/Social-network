import profile
from django.test import RequestFactory, TestCase
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser, User
from ...models import AppUser 

# https://www.section.io/engineering-education/django-unit-testing/#prerequisites
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing
class AppUserModelTest(TestCase):

  user = None

  @classmethod
  def setUp(self):
    self.user = User.objects.create_user(username='test', password='12test12', email='test@example.com')
    AppUser.objects.create(
      id=1,
      user=self.user, 
      bio='I am user0026', 
      status='In a meeting',
      profile_picture='kittens.png'
    )

  def tearDown(self):
    User.objects.all().delete()
    AppUser.objects.all().delete()

# check that the model has correct field values
  def test_ModelHasCorrectFieldValues(self):
    appuser = AppUser.objects.get(id=1)
    self.assertEqual(appuser.bio, 'I am user0026')
    self.assertEqual(appuser.status, 'In a meeting')
    self.assertEqual(appuser.profile_picture, 'kittens.png')

  # max character length of bio field
  def test_BioMaxLength(self):
    appuser = AppUser.objects.get(id=1)
    max_length = appuser._meta.get_field('bio').max_length
    self.assertEqual(max_length, 500)

  # max character length of status field
  def test_StatusMaxLength(self):
    appuser = AppUser.objects.get(id=1)
    max_length = appuser._meta.get_field('status').max_length
    self.assertEqual(max_length, 200)

  def test_ModelMethod(self):
     appuser = AppUser.objects.get(id=1)
     expected_object = self.user.username
     self.assertEqual(expected_object, str(appuser.user.username))