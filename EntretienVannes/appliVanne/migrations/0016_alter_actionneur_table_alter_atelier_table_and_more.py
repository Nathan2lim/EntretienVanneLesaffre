# Generated by Django 5.0.1 on 2024-02-13 08:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("appliVanne", "0015_vanne_enservicevanne"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="actionneur",
            table="ACTIONNEUR",
        ),
        migrations.AlterModelTable(
            name="atelier",
            table="ATELIER",
        ),
        migrations.AlterModelTable(
            name="commande",
            table="COMMANDE",
        ),
        migrations.AlterModelTable(
            name="corps",
            table="CORPS",
        ),
        migrations.AlterModelTable(
            name="fournisseur",
            table="FOURNISSEUR",
        ),
        migrations.AlterModelTable(
            name="positionneur",
            table="POSITIONNEUR",
        ),
        migrations.AlterModelTable(
            name="typepositionneur",
            table="TYPEPOSITIONNEUR",
        ),
        migrations.AlterModelTable(
            name="vanne",
            table="VANNES",
        ),
    ]
