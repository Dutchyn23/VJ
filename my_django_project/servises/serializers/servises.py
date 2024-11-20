from rest_framework import serializers

from servises.models import Servises


class ServisesSerializer(serializers.ModelSerializer):
    service_date = serializers.PrimaryKeyRelatedField(queryset=Servises.objects.all(), required=False)


    class Meta:
        model = Servises
        fields = ['service_date', 'service_type', 'equipment_id', ' comentar']


