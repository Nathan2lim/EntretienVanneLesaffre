# Generated by Django 5.0.1 on 2024-03-18 08:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("appliVanne", "0049_alter_revison_date_revision"),
    ]

    operations = [
        migrations.AlterField(
            model_name="revison",
            name="date_revision",
            field=models.DateField(
                auto_now_add=True, null=True, verbose_name="Date de la révision"
            ),
        ),
    ]
