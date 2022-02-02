from multiprocessing import context
from django.shortcuts import render
from .models import *
from .forms import *

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

def createGroup(request):
  form = GroupForm()
  if request.method == 'POST': # if user sent info
    form = GroupForm(request.POST)  # populated with the data that the user sent
    if form.is_valid(): # validate the data
      ec = EC() # add new row to ec table
      ec.ec_name = form.cleaned_data['ec_name']
      ec.save()
      return HttpResponseRedirect('/create_ec/')
    else:
      ecs = EC.objects.all()
      form = ECForm() # blank form
      return render(request, 'genedata/ec.html', {'form': form, 'ecs': ecs, 'master_genes': master_genes})
      context = {'form': form}
      return render(request, 'snapp/group_form.html', context)


