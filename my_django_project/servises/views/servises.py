from rest_framework import generics


from servises.models import Servises
from servises.serializers import ServisesSerializer

class ServisesList(generics.ListCreateAPIView):
    queryset = Servises.objects.all()
    serializer_class = ServisesSerializer

class ServisesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Servises.objects.all()
    serializer_class = ServisesSerializer

