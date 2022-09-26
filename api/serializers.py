from dataclasses import field
from rest_framework import serializers
from .models import  Persoana



class PersoanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persoana
        fields = ('id','name','surname','user','password','canUpload','canDownload')




class CreatePersoanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persoana
        fields = ('name','surname','user','password','canUpload','canDownload')



