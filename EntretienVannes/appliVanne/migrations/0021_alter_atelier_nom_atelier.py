# Generated by Django 5.0.1 on 2024-02-22 12:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("appliVanne", "0020_alter_vanne_en_service_vanne"),
    ]

    operations = [
        migrations.AlterField(
            model_name="atelier",
            name="nom_atelier",
            field=models.CharField(default="a remplir", max_length=45, unique=True),
        ),
    ]