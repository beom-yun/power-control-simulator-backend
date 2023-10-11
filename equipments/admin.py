from django.contrib import admin
from .models import Equipment, EquipmentCategory


@admin.register(EquipmentCategory)
class EquipmentCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    pass
