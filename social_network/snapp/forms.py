from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User

class GroupForm(ModelForm):
  class Meta:
    model = Group
    fields = '__all__'