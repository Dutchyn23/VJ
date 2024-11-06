from django.db import models

class Equipments(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    date_buy = models.DateTimeField()
    first_price = models.FloatField()
    depreciation_rate = models.FloatField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'