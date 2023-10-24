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
        "room",
        "name",
        "status",
        "serial_number",
    )
