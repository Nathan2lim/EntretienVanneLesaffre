# Generated by Django 5.0.1 on 2024-02-09 12:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "appliVanne",
            "0011_rename_actionneurdoubleeffet_actionneur_actionneursimpldoubleeffet_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="corps",
            name="id",
        ),
        migrations.AlterField(
            model_name="corps",
            name="idCorps",
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name="vanne",
            name="idCorps",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="appliVanne.corps",
            ),
        ),
    ]
