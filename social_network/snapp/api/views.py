from tokenize import group
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snapp.models import *
from .serializers import *
from snapp.api import serializers

# tells the user how the api works - what urls to use
@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/groups',
        'GET /api/groups/:id'  # get a 
    ]
    return Response(routes)


@api_view(['GET'])
def getGroups(request):
    groups = Group.objects.all()
    serializer = GroupSerializer(groups, many=True) # many - multiple objects to serialize
    return Response(serializer.data)


@api_view(['GET'])
def getGroup(request, pk):
    group = Group.objects.get(id=pk)
    serializer = GroupSerializer(group, many=False)
    return Response(serializer.data)