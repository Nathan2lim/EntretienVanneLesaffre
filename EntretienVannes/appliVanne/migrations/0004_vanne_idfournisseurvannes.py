# Generated by Django 5.0.1 on 2024-02-05 07:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("appliVanne", "0003_alter_commande_idcommande"),
    ]

    operations = [
        migrations.AddField(
            model_name="vanne",
            name="idFournisseurVannes",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to="appliVanne.fournisseur",
            ),
        ),
    ]
