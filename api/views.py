from django import views
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import  CreatePersonSerializer, PersonSerializer
from api.models import  Person, sha256Encode

# Create your views here.




        

class PersonView(generics.ListAPIView):
     queryset = Person.objects.all()
     serializer_class = PersonSerializer


class CreatePersonView(APIView):
    serializer_class = CreatePersonSerializer
    
    # def get():
    #      serializer_class = PersoanaSerializer
    #      queryset = Persoana.objects.all()

    def post(self, request, format= None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        # print(request.data)
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            print(serializer.data)
            
            name = serializer.data.get('name')
            surname = serializer.data.get('surname')
            user = serializer.data.get('user')
            password = sha256Encode(serializer.data.get('password'))
            canUpload = serializer.data.get('canUpload')
            canDownload = serializer.data.get('canDownload')
            print(self.request.session.session_key)

            queryset = Person.objects.filter(user = user)
            if queryset.exists():
                person = queryset[0]
                person.name = name
                person.surname = surname
                person.password = password
                person.canUpload = canUpload
                person.canDownload = canDownload
                #'id','name','surname','user','password','canUpload','canDownload')

                person.save(update_fields =['name','surname','password','canUpload','canDownload'])
            else:
                person = Person(name = name, surname = surname, user = user, password= password,  canUpload = canUpload , canDownload = canDownload)
                person.save()
            return Response(PersonSerializer(person).data, status = status.HTTP_201_CREATED)
    
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
    
    # def get(self, request, format = None):
    #     serializer_class = PersoanaSerializer
    #     queryset = Persoana.objects.all()
    #     return Response(queryset)
        


