from multiprocessing import context
from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
  return render(request, 'snapp/index.html')

def home(request):
  groups = Group.objects.all() # get all groups  .get .filter .exclude
  context = {'groups': groups}
  return render(request, 'snapp/home.html', context)

def userHome(request):
  return render(request, 'snapp/userHome.html')

def group(request, pk):
  group = Group.objects.get(id=pk)
  context = {'group': group}
  return render(request, 'snapp/group.html', context)

  
