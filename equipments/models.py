from django.db import models
from common.models import CommonModel


class EquipmentCategory(CommonModel):

    """Equipment Category Model Definition"""

    class Meta:
        verbose_name_plural = "Equipment categories"

    class EquipmentTypeChoices(models.TextChoices):
        ACB = "acb", "기중차단기"
        GCB = "gcb", "가스차단기"
        VCB = "vcb", "진공차단기"
        HSCB = "hscb", "직류고속도차단기"
        DS = "ds", "단로기"
        TR = "tr", "변압기"
        SR = "sr", "정류기"
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


class Equipment(CommonModel):

    """Equipment Model Definition"""

    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE, verbose_name="기능실")
    category = models.ForeignKey(
        "equipments.EquipmentCategory", on_delete=models.CASCADE, verbose_name="종류"
    )
    name = models.CharField(max_length=10)
    serial_number = models.CharField(
        max_length=30, null=True, blank=True, verbose_name="시리얼 넘버"
    )
    status = models.BooleanField(default=False)
    cables = models.ManyToManyField("cables.Cable")
    description = models.CharField(max_length=100, null=True, blank=True)
