# Generated by Django 5.0.1 on 2024-03-18 08:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("appliVanne", "0050_alter_revison_date_revision"),
    ]

    operations = [
        migrations.AlterField(
            model_name="revison",
            name="date_revision",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Date de la révision",
            ),
        ),
    ]
