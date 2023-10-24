from django.contrib import admin
from .models import Cable


@admin.register(Cable)
class CableAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "status",
        "voltage_type",
        "voltage",
    )
