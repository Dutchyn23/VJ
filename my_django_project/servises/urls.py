from django.urls import path
from servises.views import ServisesList, ServisesDetail
from servises.views import Servises_costsList, Servises_costsDetail

urlpatterns = [
    path('api/v1/servises/', ServisesList.as_view(), name='servises_list'),
    path('api/v1/servises/<int:pk>/', ServisesDetail.as_view(), name='servises_detail'),
    path('api/v1/servises_costs/', Servises_costsList.as_view(), name='servises_costs_list'),
    path('api/v1/servises_costs/<int:pk>/', Servises_costsDetail.as_view(), name='servises_costs_detail'),
]
