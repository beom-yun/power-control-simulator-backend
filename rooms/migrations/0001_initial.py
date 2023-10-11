# Generated by Django 4.2.6 on 2023-10-11 11:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Room",
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
                        choices=[("substation", "변전소"), ("electric_room", "전기실")],
                        max_length=15,
                        verbose_name="기능실 종류",
                    ),
                ),
                ("name", models.CharField(max_length=20, verbose_name="이름")),
                (
                    "capacity",
                    models.SmallIntegerField(
                        blank=True,
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="용량[kW]",
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="주소"
                    ),
                ),
                ("drawing", models.URLField(blank=True, null=True, verbose_name="도면")),
                (
                    "description",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]