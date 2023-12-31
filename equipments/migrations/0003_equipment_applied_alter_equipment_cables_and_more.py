# Generated by Django 4.2.6 on 2023-10-25 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("cables", "0001_initial"),
        ("equipments", "0002_alter_equipmentcategory_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="equipment",
            name="applied",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="cables.cable",
            ),
        ),
        migrations.AlterField(
            model_name="equipment",
            name="cables",
            field=models.ManyToManyField(
                blank=True, related_name="Equipments", to="cables.cable"
            ),
        ),
        migrations.AlterField(
            model_name="equipment",
            name="status",
            field=models.CharField(
                choices=[("open", "개방(OPEN)"), ("close", "투입(CLOSE)")],
                default="open",
                max_length=10,
                verbose_name="상태",
            ),
        ),
        migrations.AlterField(
            model_name="equipmentcategory",
            name="type",
            field=models.CharField(
                choices=[
                    ("acb", "기중차단기(ACB)"),
                    ("gcb", "가스차단기(GCB)"),
                    ("vcb", "진공차단기(VCB)"),
                    ("hscb", "직류고속도차단기(HSCB)"),
                    ("ds", "단로기(DS)"),
                    ("tr", "변압기(TR)"),
                    ("sr", "정류기(SR)"),
                ],
                max_length=10,
                verbose_name="종류",
            ),
        ),
    ]
