from dataclasses import field
from rest_framework import serializers
from .models import  Person



class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id','name','surname','user','password','canUpload','canDownload')




class CreatePersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name','surname','user','password','canUpload','canDownload')



