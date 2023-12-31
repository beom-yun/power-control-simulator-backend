from django.contrib import admin
from .models import Equipment, EquipmentCategory


@admin.register(EquipmentCategory)
class EquipmentCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "type",
        "specification",
        "maker",
    )


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "room",
        "name",
        "status",
        "serial_number",
        "applied",
    )

    list_display_links = (
        "id",
        "room",
        "name",
    )

    list_editable = (
        "status",
        "applied",
    )
