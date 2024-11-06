from django.contrib import admin

from production_units.models import ProductionUnits

@admin.register(ProductionUnits)
class ProductionUnitsAdmin(admin.ModelAdmin):
    pass
