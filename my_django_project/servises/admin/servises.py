from django.contrib import admin

from servises.models import Servises

@admin.register(Servises)
class ServisesAdmin(admin.ModelAdmin):
    pass
