from rest_framework import serializers

from equipments.models import Equipments


class EquipmentsSerializer(serializers.ModelSerializer):


    class Meta:
        model = Equipments
        fields = ['name', 'type', 'date_buy', 'first_price', 'depreciation_rate', 'status']
