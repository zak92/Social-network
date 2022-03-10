import profile
from django.test import RequestFactory, TestCase
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser, User
from ...models import Message, Group



class MessageModelTest(TestCase):

  user = None

  @classmethod
  def setUp(self):
    self.user = User.objects.create_user(username='test', password='12test12', email='test@example.com')
    self.group = Group.objects.create(
      id=1,
      groupCreator=self.user, 
      name='Test',
      description='This is a Test group', 
    )
    
    Message.objects.create(
      id=1,
      user=self.user, 
      group=self.group,
      message='This is a a new message', 
    )

  def tearDown(self):
    User.objects.all().delete()
    Message.objects.all().delete()
    Group.objects.all().delete()

  # check that the model has the correct field names
  def test_ModelHasCorrectFieldNames(self):
    message = Message.objects.get(id=1)
    field_label_message = message._meta.get_field('message').verbose_name
    field_label_group = message._meta.get_field('group').verbose_name
    field_label_user = message._meta.get_field('user').verbose_name
    field_label_lastUpdated = message._meta.get_field('lastUpdated').verbose_name
    field_label_dateCreated = message._meta.get_field('dateCreated').verbose_name
    field_label_user = message._meta.get_field('user').verbose_name
    self.assertEqual(field_label_message, 'message')
    self.assertEqual(field_label_group, 'group')
    self.assertEqual(field_label_user, 'user')
    self.assertEqual(field_label_lastUpdated, 'lastUpdated')
    self.assertEqual(field_label_dateCreated, 'dateCreated')

  # check that the model has correct field values
  def test_ModelHasCorrectFieldValues(self):
    message = Message.objects.get(id=1)
    self.assertEqual(message.user.username, 'test')
    self.assertEqual(message.group.name, 'Test')
    self.assertEqual(message.message, 'This is a a new message')
    
  # test the model methods
  def test_ModelMethod(self):
     message = Message.objects.get(id=1)
     expected_object = message.message
     self.assertEqual(expected_object, str(message.message))