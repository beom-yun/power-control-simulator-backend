from rest_framework.serializers import ModelSerializer
from .models import Room


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = (
            "id",
            "type",
            "name",
            "capacity",
            "address",
            "drawing",
            "description",
        )
