from django.urls import path
from . import views

urlpatterns = [
    path("", views.Equipments.as_view()),
]
