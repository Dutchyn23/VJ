from rest_framework import generics

from servises.models import Servises_costs
from servises.serializers import Servises_costsSerializer

class Servises_costsList(generics.ListCreateAPIView):
    queryset = Servises_costs.objects.all()
    serializer_class = Servises_costsSerializer

class Servises_costsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Servises_costs.objects.all()
    serializer_class = Servises_costsSerializer

