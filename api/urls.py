from django.urls import path
from .views import   CreatePersonView ,PersonView

urlpatterns = [
    # path('create-bilet/', CreateBiletView.as_view()),
    # path('bilet/', BiletView.as_view()),
    path('create-person/', CreatePersonView.as_view()),
    path('person/', PersonView.as_view())
    
    #path('persoana/<int:pk>/', PersoanaView.as_view())
    #asdas
]

