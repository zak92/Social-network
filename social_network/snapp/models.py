from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # maps to User table. User table automatically provided by Django
    bio = models.TextField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    profile_picture = models.ImageField(null=True, default="user.png")     # default image 
    dateCreated = models.DateTimeField(auto_now_add=True, null=True)
    def __unicode__(self):
      return self.user.username  # username in User model
 

class Contact(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contacts", null=True)
  contacts = models.ManyToManyField(User, related_name="contact", blank=True)  # list of friends
  def __str__(self):
    return self.user.username
  def __str__(self):
    return self.contacts.username

  
class GalleryImage(models.Model):
  owner = models.ForeignKey(User, related_name="gallery", on_delete=models.SET_NULL, null=True, blank=True)  #remove related_name t get gallery to work , but api won't work
  image = models.ImageField(blank=True, null=True)
  def __unicode__(self):
    return self.owner.username
 

class Group(models.Model):
  groupCreator = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  description = models.TextField(null=True, blank=True) # use TextField for large amounts of text, null=True -> can be null, blank=True -> if any form on page - field can be blank# If you allow for blank values, you have to allow for null values since blank values are stored as null.
  members = models.ManyToManyField(User, related_name='members', blank=True) # since you already have user in Group creator -> use related_name, blank form allowed
  lastUpdated = models.DateTimeField(auto_now=True) # automatic - last updated 
  dateCreated = models.DateTimeField(auto_now_add=True) # when it was first created - initial timestamp - will never change

  class Meta:
    ordering = ['-lastUpdated', '-dateCreated'] # show the last created / updated group at the top of the page

  def __str__(self):
    return self.name


class Message(models.Model):
  user =  models.ForeignKey(User, on_delete=models.CASCADE)  # which user sends a message - oneToMany -  when a user is deleted, delete all the children(messages)
  group = models.ForeignKey(Group, on_delete=models.CASCADE) # if a room gets deleted, all the messages get deleted
  message = models.TextField()
  lastUpdated = models.DateTimeField(auto_now=True) 
  dateCreated = models.DateTimeField(auto_now_add=True) 

  def __str__(self):
    return self.message[0:40] # if the message is too long, truncate the text