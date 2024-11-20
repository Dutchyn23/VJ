from rest_framework import serializers

from production_units.models import Production_units


class Production_unitsSerializer(serializers.ModelSerializer):
    name = serializers.PrimaryKeyRelatedField(queryset=Production_units.objects.all(), required=False)


    class Meta:
        model = Production_units
        fields = ['name', 'responsible_manager']
