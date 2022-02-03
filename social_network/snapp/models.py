from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Group(models.Model):
  groupCreator = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  description = models.TextField(null=True, blank=True) # use TextField for large amounts of text, null=True -> can be null, blank=True -> if any form on page - field can be blank# If you allow for blank values, you have to allow for null values since blank values are stored as null.
  # members = 
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