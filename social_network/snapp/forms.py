from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username' , 'email', 'password1', 'password2']

class GroupForm(ModelForm):
  class Meta:
    model = Group
    fields = '__all__'
    exclude = ['groupCreator', 'members']

class UpdateUserForm(ModelForm):
  class Meta:
    model = User
    fields = ['username', 'email']

class UpdateProfileForm(ModelForm):
  class Meta:
    model = AppUser
    fields = ['bio', 'profile_picture', 'status']


class UserForm(ModelForm):
  class Meta:
    model = User
    fields = ['username',  'email', 'password']

class UploadImagesToGalleryForm(ModelForm):
  image = forms.ImageField(required=False,widget=forms.ClearableFileInput(attrs={
    'multiple': True}))
  class Meta:
    model = GalleryImage
    fields = ['image']
