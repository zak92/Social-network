from django.test import TestCase
import json
from django.urls import reverse
from rest_framework.test import APITestCase
from ..model_factories import *
from ...serializers import GalleryImageSerializer

class GalleryImageTest(APITestCase):
  user1 = None
  GalleryImageSerializer = None
 
  def setUp(self):
    # populate test database with dummy data from model_factories.py - UserFactory
    self.user1 = GalleryImageFactory()
    self.GalleryImageSerializer = GalleryImageSerializer(instance=self.user1)
    
  
  def tearDown(self):
    GalleryImage.objects.all().delete()
    GalleryImageFactory.reset_sequence(0)
   

  # check if all the necessary fields are there
  def test_GalleryImageSerializerCorrectFields(self):
    data = self.GalleryImageSerializer.data
    self.assertEqual(set(data.keys()), set(['image']))
  

  # check if all the the fields contain correct values
  def test_GalleryImageSerializerFieldData(self):
    data = self.GalleryImageSerializer.data
    # check if data is correct
    self.assertEqual(data['image'], '/images/http%3A/127.0.0.1%3A8080/images/test_image_rvDQSv4_HTMwIRR.jpg')