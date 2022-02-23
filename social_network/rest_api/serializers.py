from snapp.models import *
from rest_framework import serializers


class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class GroupListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['bio', 'status', 'profile_picture']

class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model =  GalleryImage
        fields = ['image']

class ContactsSerializer(serializers.ModelSerializer):
    contacts = UsernameSerializer(many=True)
    class Meta:
        model = Contact
        fields = ['contacts']

class GroupDetailSerializer(serializers.ModelSerializer):
    members = UsernameSerializer(many=True)
    groupCreator = UsernameSerializer()
    class Meta:
        model = Group
        fields = ['id', 'name', 'description','lastUpdated', 'dateCreated', 'groupCreator', 'members']



class UserSerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer(many=True)
    appuser = AppUserSerializer()
    gallery = GalleryImageSerializer(many=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'last_login', 'date_joined', 'appuser', 'gallery', 'contacts']

 





