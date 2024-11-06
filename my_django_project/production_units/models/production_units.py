from django.db import models

class ProductionUnits(models.Model):
    name = models.CharField(max_length=100)
    responsible_manager = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'