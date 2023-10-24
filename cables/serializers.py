from rest_framework.serializers import ModelSerializer
from .models import Cable


class CableSerializer(ModelSerializer):
    class Meta:
        model = Cable
        fields = (
            "id",
            "status",
            "voltage_type",
            "voltage",
            "specification",
            "description",
        )
