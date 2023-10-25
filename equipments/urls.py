from django.urls import path
from .views import Equipments, EquipmentStatusChange

urlpatterns = [
    path("", Equipments.as_view()),
    path("change/", EquipmentStatusChange.as_view()),
]
