# Generated by Django 5.0.1 on 2024-02-12 10:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("appliVanne", "0014_alter_vanne_numerocommande"),
    ]

    operations = [
        migrations.AddField(
            model_name="vanne",
            name="enServiceVanne",
            field=models.BooleanField(default=1),
        ),
    ]