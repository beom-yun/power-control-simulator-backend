# Generated by Django 4.2.6 on 2023-10-11 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("cables", "0001_initial"),
        ("rooms", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="EquipmentCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("acb", "기중차단기"),
                            ("gcb", "가스차단기"),
                            ("vcb", "진공차단기"),
                            ("hscb", "직류고속도차단기"),
                            ("ds", "단로기"),
                            ("tr", "변압기"),
                            ("sr", "정류기"),
                        ],
                        max_length=10,
                        verbose_name="종류",
                    ),
                ),
                (
                    "specification",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="규격"
                    ),
                ),
                ("photo", models.URLField(blank=True, null=True)),
                ("maker", models.CharField(blank=True, max_length=100, null=True)),
                ("manual", models.URLField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Equipment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=10)),
                (
                    "serial_number",
                    models.CharField(
                        blank=True, max_length=30, null=True, verbose_name="시리얼 넘버"
                    ),
                ),
                ("status", models.BooleanField(default=False)),
                (
                    "description",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("cables", models.ManyToManyField(to="cables.cable")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="equipments.equipmentcategory",
                        verbose_name="종류",
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rooms.room",
                        verbose_name="기능실",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
