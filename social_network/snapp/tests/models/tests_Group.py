import profile
from django.test import RequestFactory, TestCase
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser, User
from ...models import Group


class GroupModelTest(TestCase):

  user = None

  @classmethod
  def setUp(self):
    self.user = User.objects.create_user(username='test', password='12test12', email='test@example.com')
    Group.objects.create(
      id=1,
      groupCreator=self.user, 
      name='Test',
      description='This is a Test group', 
    )

  def tearDown(self):
    User.objects.all().delete()
    Group.objects.all().delete()

# check that the model has the correct field names
  def test_ModelHasCorrectFieldNames(self):
    group = Group.objects.get(id=1)
    field_label_groupCreator = group._meta.get_field('groupCreator').verbose_name
    field_label_name = group._meta.get_field('name').verbose_name
    field_label_description = group._meta.get_field('description').verbose_name
    field_label_members = group._meta.get_field('members').verbose_name
    field_label_lastUpdated = group._meta.get_field('lastUpdated').verbose_name
    field_label_dateCreated = group._meta.get_field('dateCreated').verbose_name
    self.assertEqual(field_label_groupCreator, 'groupCreator')
    self.assertEqual(field_label_name, 'name')
    self.assertEqual(field_label_members, 'members')
    self.assertEqual(field_label_description, 'description')
    self.assertEqual(field_label_lastUpdated, 'lastUpdated')
    self.assertEqual(field_label_dateCreated, 'dateCreated')

# check that the model has correct field values
  def test_ModelHasCorrectFieldValues(self):
    group = Group.objects.get(id=1)
    self.assertEqual(group.groupCreator.username, 'test')
    self.assertEqual(group.name, 'Test')
    self.assertEqual(group.description, 'This is a Test group')

    
  # max character length of name field
  def test_BioMaxLength(self):
    group = Group.objects.get(id=1)
    max_length = group._meta.get_field('name').max_length
    self.assertEqual(max_length, 200)


  # test the model methods
  def test_ModelMethod(self):
     group = Group.objects.get(id=1)
     expected_object = group.name
     self.assertEqual(expected_object, str(group.name))