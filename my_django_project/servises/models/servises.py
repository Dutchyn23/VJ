from django.db import models

from equipments.models import Equipments


class Servises(models.Model):
    service_date = models.DateTimeField()
    service_type = models.CharField(max_length=100)
    equipment_id =models.ForeignKey(Equipments, on_delete=models.CASCADE)
    comentar = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.service_date}'