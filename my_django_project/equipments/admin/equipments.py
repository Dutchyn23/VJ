from django.contrib import admin

from equipments.models import Equipments

@admin.register(Equipments)
class EquipmentsAdmin(admin.ModelAdmin):
    pass
