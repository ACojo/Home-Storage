from dataclasses import field
from rest_framework import serializers
from .models import Bilet, Persoana

class BiletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bilet
        fields = ('id', 'code','price','start_station','stop_station','current_time')

class PersoanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persoana
        fields = ('id','name','surname','id_card')


class CreatePersoanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persoana
        fields = ('name','surname','id_card')

class CreateBiletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bilet 
        fields = ('price','start_station','stop_station')
