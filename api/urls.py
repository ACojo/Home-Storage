from django.urls import path
from .views import   CreatePersoanaView ,PersoanaView

urlpatterns = [
    # path('create-bilet/', CreateBiletView.as_view()),
    # path('bilet/', BiletView.as_view()),
    path('create-persoana/', CreatePersoanaView.as_view()),
    path('persoana/', PersoanaView.as_view())
    
    #path('persoana/<int:pk>/', PersoanaView.as_view())
    #asdas
]

