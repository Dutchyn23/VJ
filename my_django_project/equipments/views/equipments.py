from rest_framework import generics


from equipments.models import Equipments
from equipments.serializers import EquipmentsSerializer

class EquipmentsList(generics.ListCreateAPIView):
    queryset = Equipments.objects.all()
    serializer_class = EquipmentsSerializer

class EquipmentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipments.objects.all()
    serializer_class = EquipmentsSerializer

