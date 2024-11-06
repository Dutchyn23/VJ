from django.db import models


from servises.models import Servises


class Servises_Costs(models.Model):
    servises_id =models.ForeignKey(Servises, on_delete=models.CASCADE)
    sum = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()


    def __str__(self):
        return f'{self.sum}'