from rest_framework.serializers import ModelSerializer, CharField
from .models import Equipment, EquipmentCategory
from rooms.serializers import RoomSerializer
from cables.serializers import CableSerializer


class EquipmentCategorySerializer(ModelSerializer):
    class Meta:
        model = EquipmentCategory
        fields = (
            "id",
            "type",
            "specification",
            "photo",
            "maker",
            "manual",
        )


class EquipmentSerializer(ModelSerializer):
    room = RoomSerializer(read_only=True)
    category = EquipmentCategorySerializer(read_only=True)
    cables = CableSerializer(read_only=True, many=True)

    class Meta:
        model = Equipment
        fields = (
            "id",
            "name",
            "serial_number",
            "status",
            "description",
            "room",
            "category",
            "cables",
        )


class EquipmentStatusChangeSerializer(ModelSerializer):
    change = CharField(max_length=10)

    class Meta:
        model = Equipment
        fields = (
            "id",
            "change",
        )
