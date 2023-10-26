from django.contrib import admin
from .models import Cable


@admin.register(Cable)
class CableAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "status",
        "voltage_type",
        "voltage",
    )

    list_display_links = (
        "id",
        "voltage_type",
        "voltage",
    )

    list_editable = ("status",)
