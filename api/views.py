from django import views
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BiletSerializer, CreatePersoanaSerializer, PersoanaSerializer, CreateBiletSerializer
from api.models import Bilet, Persoana

# Create your views here.

class BiletView(generics.ListAPIView):
    queryset = Bilet.objects.all()
    serializer_class = BiletSerializer



class CreateBiletView(APIView):
    serializer_class = CreateBiletSerializer

    def post(self, request, format = None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            price = serializer.data.get('price')
            start_station = serializer.data.get('start_station')
            stop_station = serializer.data.get('stop_station')

            ticket = Bilet(price = price, start_station = start_station, stop_station = stop_station)
            ticket.save()
            return Response(BiletSerializer(ticket).data, status = status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format = None):
        queryset = Bilet.objects.all()
        codes = [bilet.code for bilet in Bilet.objects.all()]
        bilete = Bilet.objects.all().values('code','price','start_station','stop_station','current_time')
        bilete_list = list(bilete)
        return JsonResponse(bilete_list, safe = False)
        #return  Response(codes, status = status.HTTP_200_OK)
        

class PersoanaView(generics.ListAPIView):
    queryset = Persoana.objects.all()
    serializer_class = PersoanaSerializer


class CreatePersoanaView(APIView):
    serializer_class = CreatePersoanaSerializer
    
    # def get():
    #     serializer_class = PersoanaSerializer
    #     queryset = Persoana.objects.all()

    def post(self, request, format= None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        # print(request.data)
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            print(serializer.data)
            name = serializer.data.get('name')
            surname = serializer.data.get('surname')
            id_card = serializer.data.get('id_card')
            print(self.request.session.session_key)

            queryset = Persoana.objects.filter(name = name, surname = surname)
            if queryset.exists():
                person = queryset[0]
                person.name = name
                person.surname = surname
                person.id_card = id_card
                person.save(update_fields =['id_card'])
            else:
                person = Persoana(name = name, surname = surname, id_card = id_card)
                person.save()
            return Response(PersoanaSerializer(person).data, status = status.HTTP_201_CREATED)
    
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)


