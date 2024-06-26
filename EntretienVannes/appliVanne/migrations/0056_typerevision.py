# Generated by Django 5.0.1 on 2024-03-19 07:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("appliVanne", "0055_alter_positionneur_fonctionnement_positionneur"),
    ]

    operations = [
        migrations.CreateModel(
            name="TypeRevision",
            fields=[
                (
                    "id_type_revision",
                    models.AutoField(
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="ID du type de révision",
                    ),
                ),
                (
                    "type_revision",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Type de révision"
                    ),
                ),
            ],
            options={
                "db_table": "TYPEREVISION",
            },
        ),
    ]
