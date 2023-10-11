from django.db import models
from django.core.validators import MinValueValidator
from common.models import CommonModel


class Room(CommonModel):

    """Rooms Model Definition"""

    class RoomTypeChoices(models.TextChoices):
        SS = "substation", "변전소"
        ER = "electric_room", "전기실"

    type = models.CharField(
        max_length=15, choices=RoomTypeChoices.choices, verbose_name="기능실 종류"
    )
    name = models.CharField(max_length=20, verbose_name="이름")
    capacity = models.SmallIntegerField(
        validators=[MinValueValidator(0)], null=True, blank=True, verbose_name="용량[kW]"
    )
    address = models.CharField(max_length=100, null=True, blank=True, verbose_name="주소")
    drawing = models.URLField(null=True, blank=True, verbose_name="도면")
    description = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.name}{self.get_type_display()}"
