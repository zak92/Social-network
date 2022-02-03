from snapp.models import *
from rest_framework.serializers import ModelSerializer



class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'