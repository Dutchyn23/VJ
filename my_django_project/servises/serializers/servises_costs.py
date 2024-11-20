from rest_framework import serializers

from servises.models import Servises_Costs


class Servises_costsSerializer(serializers.ModelSerializer):
    servises_id = serializers.PrimaryKeyRelatedField(queryset=Servises_Costs.objects.all(), required=False)


    class Meta:
        model = Servises_Costs
        fields = ['servises_id', 'sum', 'date', ' description']



