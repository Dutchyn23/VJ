from rest_framework import generics


from production_units.models import Production_unit
from production_units.serializers import Production_unitSerializer

class Production_unitsList(generics.ListCreateAPIView):
    queryset = Production_unit.objects.all()
    serializer_class = Production_unitSerializer

class Production_unitsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Production_unit.objects.all()
    serializer_class = Production_unitSerializer

