# Generated by Django 5.0.1 on 2024-03-07 13:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("appliVanne", "0039_alter_vanne_date_commande"),
    ]

    operations = [
        migrations.AddField(
            model_name="vanne",
            name="date_commande_bis",
            field=models.DateField(
                blank=True, default=datetime.date(1222, 1, 1), null=True
            ),
        ),
    ]
