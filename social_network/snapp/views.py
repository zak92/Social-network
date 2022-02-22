from email import message
from multiprocessing import context
import profile
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *

# Create your views here.

def userLogin(request):
  page = 'login'
  if request.user.is_authenticated:  # cant go to login page
    return redirect('home')

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
      return redirect('home')
    else:
      messages.error(request, 'Incorrect username or password')

  context = {'page': page}
  return render(request, 'snapp/index.html', context)


def userLogout(request):
  logout(request) # delete session token
  return redirect('home')

def userSignUp(request):
  form = MyUserCreationForm()
  if request.method == 'POST':
    
     form = MyUserCreationForm(request.POST)  # pass indata that the user sent - 
     if form.is_valid(): # validate the data
      user = form.save(commit=False)  # save data and get user object and clean data
      user.username = user.username.lower() # username must be in lowercase
      user.save()
      AppUser.objects.create(user=user)
      login(request, user) # log user in immediately
     
      return redirect('home')
     else:
      messages.error(request, 'Error in user registration / sign up')
  context = {'form': form}
  return render(request, 'snapp/index.html', context)

# @login_required(login_url='login')
def userProfile(request, pk):
 
  user = User.objects.get(id=pk)
  current_user = request.user
  first_contact = Contact.objects.get_or_create(
  user=user
  )
  contact = Contact.objects.get(user=user)
  contacts = contact.contacts.all()
  print(user)

  # print(current_user.id)
  groups = user.group_set.all() #.order_by('-dateCreated') 
  group_messages = user.message_set.all()
 
  if request.method == 'POST' and 'add' in request.POST: # if user sent info
    active_user = Contact.objects.get(user=request.user)
    active_user.contacts.add(user)
    return redirect('user-profile', pk=current_user.id)
    
  if request.method == 'POST' and 'remove' in request.POST: # if user sent info
    active_user = Contact.objects.get(user=request.user)
    active_user.contacts.remove(user)
    
  context = {'user': user, 'groups':groups, 'group_messages': group_messages , 'contacts': contacts}
  return render(request, 'snapp/user_profile.html', context)

def home(request):
  q = request.GET.get('q') if request.GET.get('q') != None else ''
  groups = Group.objects.filter(
     Q(name__icontains=q) |                                                                                # FIX VIEWS - REFER TO CODING EXERCISES
     Q(description__icontains=q)
    ) 
  
  group_count = groups.count()
  f =  request.GET.get('f') if request.GET.get('f') != None else ''
  users = User.objects.filter(
     Q(username__icontains=f)                                                                             # FIX VIEWS - REFER TO CODING EXERCISES
    )
  
  context = {'groups': groups, 'group_count': group_count, 'users': users}
  return render(request, 'snapp/home.html', context)



def group(request, pk):
  group = Group.objects.get(id=pk)
  groupMessages = group.message_set.all().order_by('-dateCreated')   # )set -> many-to-many relation ; message -> Model name (lowercase) - give all children of that model - newest will be first
  members = group.members.all()

  if request.method == 'POST': # if user sent info
    message = Message.objects.create(
      user=request.user,
      group=group,
      message=request.POST.get('messageBody')
    )
    group.members.add(request.user)   # add user to group when they comment
    return redirect('group', pk=group.id)

  
  context = {'group': group, 
             'groupMessages': groupMessages, 
             'members':members
             }
  return render(request, 'snapp/group.html', context)

@login_required(login_url='login')  # redirect to login page
def createGroup(request):
  form = GroupForm()
  if request.method == 'POST': # if user sent info
    form = GroupForm(request.POST)  # populated with the data that the user sent
    if form.is_valid(): # validate the data
      group = form.save(commit=False)
      group.groupCreator = request.user
      group.save()
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


@login_required(login_url='login')
def deleteMessage(request, pk):
  message = Message.objects.get(id=pk)

  if request.user != message.user:  # if user is not the creator of message - they cannot delete it
    return HttpResponse('You cannot delete since you did not create the message')

  if request.method == 'POST':
    message.delete()
    return redirect('home')
  return render(request, 'snapp/delete.html', {'obj': message})

@login_required(login_url='login')
def updateProfile(request):
 
  #user = User.objects.get(id=pk)
  #form = UserProfileForm(instance=user)
  user_form = UpdateUserForm(instance=request.user)
  profile_form = UpdateProfileForm(instance=request.user.appuser)
  current_user = request.user

  #profile_form = UpdateProfileForm(instance=user)
  if request.method == 'POST': # if user sent info
    user_form = UpdateUserForm(request.POST, request.FILES, instance=request.user)  # populated with the data that the user sent - update a room, do not create a new one
    profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.appuser)
    if user_form.is_valid() and profile_form.is_valid(): # validate the data
      user_form.save()
      profile_form.save()
      return redirect('user-profile', pk=current_user.id)
  context = {'user_form': user_form, 'profile_form': profile_form}
  return render(request, 'snapp/user_profile_settings.html', context)

# @login_required(login_url='login')
# def myProfile(request):
#   user = request.user
#   #appuser = AppUser.objects.create(user=request.user)
#   #appuser = request.user.appuser
#   #friends = user.appuser.friends.all()
#   groups = user.group_set.all() #.order_by('-dateCreated') 
#   group_messages = user.message_set.all()
 
#   context = {'user':user,'groups':groups, 'group_messages': group_messages}
#   return render(request, 'snapp/user_profile.html', context)

@login_required(login_url='login')
def imageGallery(request):
  user = request.user
  images = user.galleryimage_set.all()
 
  #images = GalleryImage.objects.all()
  gallery_form = UploadImagesToGalleryForm() 
  if request.method == 'POST': # if user sent info
    gallery_form = UploadImagesToGalleryForm(request.POST, request.FILES, instance=user)
    files = request.FILES.getlist('image')
    if gallery_form.is_valid(): # validate the data
      new_image = gallery_form.save(commit=False)
      new_image.owner = request.user
      new_image.save()
      #GalleryImage.objects.create(galleryOwner=user, image=request.FILES.getlist('image'))
#       #print(user)
      for f in files:
        # img = GalleryImage(image=f)
        # img.save()
        # new_image.image.add(img)
        # new_image.save()
        photo = GalleryImage.objects.create(owner=user, image=f)
      gallery_form.save()
      
      return redirect('imageGallery')
     
  context = {'user':user, 'gallery_form':gallery_form, 'images':images}
  return render(request, 'snapp/image_gallery.html', context)

def viewImageGallery(request, pk):
  user = User.objects.get(username=pk)
  images = user.galleryimage_set.all()
     
  context = {'user':user, 'images':images}
  return render(request, 'snapp/image_gallery.html', context)


