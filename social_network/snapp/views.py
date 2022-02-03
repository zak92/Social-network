from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *

# Create your views here.

def userLogin(request):
  page = 'login'
  if request.user.is_authenticated:  # cant go to login page
    return redirect('userHome')

  if request.method == 'POST': # if user sent info
    username = request.POST.get('username').lower()  # populated with the data that the user sent
    password = request.POST.get('password')
    
    try:
      user = User.objects.get(username=username)
    except:
      messages.error(request, 'User does not exist - PLease create an account')  # flash messages

    user = authenticate(request, username=username, password=password) # authenticate user - return user object

    if user is not None:
      login(request, user) # activate session - user is logged in
      return redirect('userHome')
    else:
      messages.error(request, 'Incorrect username or password')

  context = {'page': page}
  return render(request, 'snapp/index.html', context)


def userLogout(request):
  logout(request) # delete session token
  return redirect('home')

def userSignUp(request):
  form = UserCreationForm()
  if request.method == 'POST':
     form = UserCreationForm(request.POST)  # pass indata that the user sent
     if form.is_valid(): # validate the data
      user = form.save(commit=False)  # save data and get user object and clean data
      user.username = user.username.lower() # username must be in lowercase
      user.save()
      login(request, user) # log user in immediately
      return redirect('userHome')
     else:
      messages.error(request, 'Error in user registration / sign up')
  context = {'form': form}
  return render(request, 'snapp/index.html', context)

def home(request):
  q = request.GET.get('q') if request.GET.get('q') != None else ''

  groups = Group.objects.filter(
     Q(name__icontains=q) |                                                                                # FIX VIEWS - REFER TO CODING EXERCISES
     Q(description__icontains=q)
    ) # get all groups  .get .filter .exclude
  # groups = Group.objects.filter(name__icontains=q)
  group_count = groups.count()
  context = {'groups': groups, 'group_count': group_count}
  return render(request, 'snapp/home.html', context)

@login_required(login_url='login')
def userHome(request):
  return render(request, 'snapp/userHome.html')

def group(request, pk):
  group = Group.objects.get(id=pk)
  context = {'group': group}
  return render(request, 'snapp/group.html', context)

@login_required(login_url='login')  # redirect to login page
def createGroup(request):
  form = GroupForm()
  if request.method == 'POST': # if user sent info
    form = GroupForm(request.POST)  # populated with the data that the user sent
    if form.is_valid(): # validate the data
      form.save()
      return redirect('home')
  context = {'form': form}
  return render(request, 'snapp/group_form.html', context)

@login_required(login_url='login')
def updateGroup(request, pk):
  group = Group.objects.get(id=pk)
  form = GroupForm(instance=group) # the form will be prefilled with data about the group

  if request.user != group.groupCreator:  # if user is not the creator of room - they cannot update it
    return HttpResponse('You cannot update since you did not create the group')

  if request.method == 'POST': # if user sent info
    form = GroupForm(request.POST,instance=group)  # populated with the data that the user sent - update a room, do not create a new one
    if form.is_valid(): # validate the data
      form.save()
      return redirect('home')
  context = {'form': form}
  return render(request, 'snapp/group_form.html', context)

@login_required(login_url='login')
def deleteGroup(request, pk):
  group = Group.objects.get(id=pk)

  if request.user != group.groupCreator:  # if user is not the creator of room - they cannot delete it
    return HttpResponse('You cannot delete since you did not create the group')

  if request.method == 'POST':
    group.delete()
    return redirect('home')
  return render(request, 'snapp/delete.html', {'obj': group})

