from django.db import models
from common.models import CommonModel


class EquipmentCategory(CommonModel):

    """Equipment Category Model Definition"""

    class Meta:
        verbose_name_plural = "Equipment categories"

    class EquipmentTypeChoices(models.TextChoices):
        ACB = "acb", "기중차단기(ACB)"
        GCB = "gcb", "가스차단기(GCB)"
        VCB = "vcb", "진공차단기(VCB)"
        HSCB = "hscb", "직류고속도차단기(HSCB)"
        DS = "ds", "단로기(DS)"
        TR = "tr", "변압기(TR)"
        SR = "sr", "정류기(SR)"
        # VSS
        # ATS

    type = models.CharField(
        max_length=10, choices=EquipmentTypeChoices.choices, verbose_name="종류"
    )
    specification = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="규격"
    )
    photo = models.URLField(null=True, blank=True)
    maker = models.CharField(max_length=100, null=True, blank=True)
    manual = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.type} {self.specification} {self.maker}"


class Equipment(CommonModel):

    """Equipment Model Definition"""

    class EquipmentStatusChoices(models.TextChoices):
        OPEN = "open", "개방(OPEN)"
        CLOSE = "close", "투입(CLOSE)"

    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE, verbose_name="기능실")
    category = models.ForeignKey(
        "equipments.EquipmentCategory", on_delete=models.CASCADE, verbose_name="종류"
    )
    name = models.CharField(max_length=10)
    serial_number = models.CharField(
        max_length=30, null=True, blank=True, verbose_name="시리얼 넘버"
    )
    status = models.CharField(
        max_length=10,
        choices=EquipmentStatusChoices.choices,
        verbose_name="상태",
        default=EquipmentStatusChoices.OPEN,
    )
    cables = models.ManyToManyField("cables.Cable", blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.room} {self.name}"

    def check_status(self, query):
        print(f"check status : {self.name}, {self.status} -> {query.change}")
        if self.category == EquipmentCategory.EquipmentTypeChoices.ACB:
            pass
        elif self.category == EquipmentCategory.EquipmentTypeChoices.GCB:
            pass
        elif self.category == EquipmentCategory.EquipmentTypeChoices.VCB:
            pass
        elif self.category == EquipmentCategory.EquipmentTypeChoices.HSCB:
            pass
        elif self.category == EquipmentCategory.EquipmentTypeChoices.DS:
            pass
        elif self.category == EquipmentCategory.EquipmentTypeChoices.TR:
            pass
        elif self.category == EquipmentCategory.EquipmentTypeChoices.SR:
            pass
