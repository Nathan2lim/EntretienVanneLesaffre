# Generated by Django 5.0.1 on 2024-03-06 10:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("appliVanne", "0032_alter_actionneur_taille_actionneur_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="revison",
            name="id_revison_vanne",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
