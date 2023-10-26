from collections import deque
from django.db import transaction
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.exceptions import NotFound, ParseError
from .models import Equipment, EquipmentCategory
from .serializers import EquipmentSerializer, EquipmentStatusChangeSerializer


class Equipments(APIView):
    def get(self, request):
        all_equipments = Equipment.objects.all()
        serializer = EquipmentSerializer(all_equipments, many=True)
        return Response(serializer.data)


class EquipmentStatusChange(APIView):
    def get_object(self, pk):
        try:
            return Equipment.objects.get(id=pk)
        except Equipment.DoesNotExist:
            raise NotFound("존재하지 않는 Equipment 입니다.")

    def put(self, request):
        equipment = self.get_object(request.data.get("id", ""))
        serializer = EquipmentStatusChangeSerializer(equipment, data=request.data)
        if serializer.is_valid():
            change = request.data.get("change")
            res = self.check_status(equipment, change)
            print(res)
            if res.get("ok"):
                eq_serializer = EquipmentSerializer(
                    equipment, data={"status": change}, partial=True
                )
                if eq_serializer.is_valid():
                    updated_equipment = eq_serializer.save()
                    return Response(EquipmentSerializer(updated_equipment).data)
                else:
                    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
            else:
                raise ParseError(res.get("detail"))
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def check_status(self, equipment, change):
        with transaction.atomic():
            print(f"check status : {equipment.name}, {equipment.status} -> {change}")
            # 현재상태랑 같은 요청이 들어오면 무시(제어 안함)
            if equipment.status == change:
                return {
                    "ok": False,
                    "detail": f"{equipment.name} 현재 {equipment.status} 상태입니다.",
                }
            ###

            eq_q, cable_result = deque([equipment]), set()
            while eq_q:
                eq = eq_q.popleft()
                print("[eq] :", eq, ", [category] :", eq.category.type)

                if eq.category.type == EquipmentCategory.EquipmentTypeChoices.ACB:
                    pass

                elif eq.category.type == EquipmentCategory.EquipmentTypeChoices.GCB:
                    if change == "close":
                        cables = eq.cables.all()

                        # 양 측이 가압중이면 제어 불가
                        flag = True
                        for cable in cables:
                            flag = flag and cable.status
                        if flag:
                            return {"ok": False, "detail": f"{eq} 양 측이 가압중입니다."}
                        ###

                        # 양 측이 가압중이지 않으면 그냥 CLOSE
                        flag = False
                        for cable in cables:
                            flag = flag or cable.status
                        if not flag:
                            return {"ok": True}
                        ###

                        # CLOSE한 해당 기기에 연결된 케이블들 중, 가압이 안된 케이블에 가압 실시
                        # 그 케이블에 연결된 기기들 중, CLOSE 상태였던 것들에 대해 반복 실시
                        for cable in cables:
                            if not cable.status:
                                cable.status = True
                                cable.save()
                                cable_result.add(cable)
                                for next_eq in cable.equipments.exclude(id=eq.id):
                                    if next_eq.status == "close":
                                        eq_q.append(next_eq)
                                    elif (
                                        next_eq.category.type
                                        == EquipmentCategory.EquipmentTypeChoices.TR
                                    ):
                                        eq_q.append(next_eq)
                            else:
                                eq.applied = cable
                                eq.save()
                        ###

                    elif change == "open":
                        cables = eq.cables.all()

                        # 양 측이 가압중이지 않으면 그냥 OPEN
                        flag = False
                        for cable in cables:
                            flag = flag or cable.status
                        if not flag:
                            return {"ok": True}
                        ###

                        # OPEN한 해당 차단기의 연결된 케이블들 중, 2차측의 케이블 무가압 실시
                        # 그 케이블에 연결된 기기들 중, CLOSE 상태였던 것들에 대해 반복 실시
                        for cable in cables:
                            if cable != eq.applied:
                                cable.status = False
                                cable.save()
                                eq.applied = None
                                eq.save()
                                cable_result.add(cable)
                                for next_eq in cable.equipments.exclude(id=eq.id):
                                    if next_eq.status == "close":
                                        eq_q.append(next_eq)
                                    elif (
                                        next_eq.category.type
                                        == EquipmentCategory.EquipmentTypeChoices.TR
                                    ):
                                        eq_q.append(next_eq)

                elif eq.category.type == EquipmentCategory.EquipmentTypeChoices.VCB:
                    pass

                elif eq.category.type == EquipmentCategory.EquipmentTypeChoices.HSCB:
                    pass

                elif eq.category.type == EquipmentCategory.EquipmentTypeChoices.DS:
                    pass

                elif eq.category.type == EquipmentCategory.EquipmentTypeChoices.TR:
                    if change == "close":
                        eq.status = "close"
                        eq.save()
                        cables = eq.cables.all()
                        for cable in cables:
                            if not cable.status:
                                cable.status = True
                                cable.save()
                                cable_result.add(cable)
                                for next_eq in cable.equipments.exclude(id=eq.id):
                                    if next_eq.status == "close":
                                        eq_q.append(next_eq)
                            else:
                                eq.applied = cable
                                eq.save()

                    elif change == "open":
                        eq.status = "open"
                        eq.save()
                        cables = eq.cables.all()
                        for cable in cables:
                            if cable != eq.applied:
                                cable.status = False
                                cable.save()
                                eq.applied = None
                                eq.save()
                                cable_result.add(cable)
                                for next_eq in cable.equipments.exclude(id=eq.id):
                                    if next_eq.status == "close":
                                        eq_q.append(next_eq)

                elif eq.category.type == EquipmentCategory.EquipmentTypeChoices.SR:
                    pass

            print(cable_result, "to", change)
            return {"ok": True}
