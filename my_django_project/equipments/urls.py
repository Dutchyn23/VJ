from django.urls import path
from equipments.views import EquipmentsList, EquipmentsDetail

urlpatterns = [
    path('api/v1/equipments/', EquipmentsList.as_view(), name='equipments_list'),
    path('api/v1/equipmets/<int:pk>/', EquipmentsDetail.as_view(), name='equipments_detail'),
]
