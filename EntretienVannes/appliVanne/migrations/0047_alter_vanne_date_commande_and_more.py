# Generated by Django 5.0.1 on 2024-03-15 08:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("appliVanne", "0046_revison_detail_commentaire"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vanne",
            name="date_commande",
            field=models.DateField(
                blank=True,
                default=datetime.date(2001, 1, 1),
                null=True,
                verbose_name="Date de la commande",
            ),
        ),
        migrations.AlterField(
            model_name="vanne",
            name="derniere_revision",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Date de la dernière révision"
            ),
        ),
        migrations.AlterField(
            model_name="vanne",
            name="voir_en",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Date de la prochaine révision"
            ),
        ),
    ]
