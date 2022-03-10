import profile
from django.test import RequestFactory, TestCase
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser, User
from ...models import Contact

class ContactModelTest(TestCase):

  user = None

  @classmethod
  def setUp(self):
    self.user = User.objects.create_user(username='test', password='12test12', email='test@example.com')
    Contact.objects.create(
      id=1,
      user = self.user, 
    )

  def tearDown(self):
    User.objects.all().delete()
    Contact.objects.all().delete()

  def test_ModelHasCorrectFieldNames(self):
    contact = Contact.objects.get(id=1)
    field_label_user = contact._meta.get_field('user').verbose_name
    field_label_contacts = contact._meta.get_field('contacts').verbose_name
    self.assertEqual(field_label_user, 'user')
    self.assertEqual(field_label_contacts, 'contacts')

  #check that the model has correct field values
  def test_ModelHasCorrectFieldValues(self):
    contact = Contact.objects.get(id=1)
    contacts = contact.contacts.all()
    self.assertEqual(contact.user.username, 'test')
  
# test model methods
  def test_ModelMethod(self):
    contact = Contact.objects.get(id=1)
    expected_object = self.user.username
    self.assertEqual(expected_object, str(contact.user.username)) 
    