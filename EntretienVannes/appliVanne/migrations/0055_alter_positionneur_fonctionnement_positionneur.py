# Generated by Django 5.0.1 on 2024-03-18 10:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("appliVanne", "0054_alter_actionneur_actionneur_simpl_double_effet_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="positionneur",
            name="fonctionnement_positionneur",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="appliVanne.typepositionneur",
                verbose_name="Fonctionnement du positionneur",
            ),
        ),
    ]
