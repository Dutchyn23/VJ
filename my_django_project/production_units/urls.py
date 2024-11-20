from django.urls import path
from production_units.views import Production_unitsList, Production_unitsDetail

urlpatterns = [
    path('api/v1/production_units/',Production_unitsList.as_view(), name='production_units_list'),
    path('api/v1/production_units/<int:pk>/', Production_unitsDetail.as_view(), name='production_units_detail'),
]
