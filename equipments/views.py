from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Equipment
from .serializers import EquipmentSerializer


class Equipments(APIView):
    def get(self, request):
        all_equipments = Equipment.objects.all()
        serializer = EquipmentSerializer(all_equipments, many=True)
        return Response(serializer.data)
