# Generated by Django 5.0.1 on 2024-03-06 07:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("appliVanne", "0031_revison"),
    ]

    operations = [
        migrations.AlterField(
            model_name="actionneur",
            name="taille_actionneur",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="corps",
            name="cv_corps",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="corps",
            name="dn_corps",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="corps",
            name="pn_corps",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
