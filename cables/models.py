from django.db import models
from django.core.validators import MinValueValidator
from common.models import CommonModel


class Cable(CommonModel):

    """Cable Model Definition"""

    class VoltageTypeChoices(models.TextChoices):
        AC = "ac", "AC"
        DC = "dc", "DC"

    status = models.BooleanField(default=False, verbose_name="상태")
    voltage_type = models.CharField(
        max_length=2,
        choices=VoltageTypeChoices.choices,
        null=True,
        blank=True,
        verbose_name="전압 종류",
    )
    voltage = models.SmallIntegerField(
        validators=[MinValueValidator(0)], null=True, blank=True, verbose_name="전압[V]"
    )
    specification = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="규격"
    )
    # primary = models.ManyToManyField("equipments.Equipment", verbose_name="1차측")
    # secondary = models.ManyToManyField("equipments.Equipment", verbose_name="2차측")
    description = models.CharField(max_length=100, null=True, blank=True)

    # def __str__(self):
    #     return f"{primary} - {secondary}"
