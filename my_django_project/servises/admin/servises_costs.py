from django.contrib import admin

from servises.models import Servises_Costs

@admin.register(Servises_Costs)
class Servises_CostsAdmin(admin.ModelAdmin):
    pass
