# Generated by Django 5.0.1 on 2024-02-26 10:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("appliVanne", "0022_alter_actionneur_id_actionneur_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="positionneur",
            old_name="femer_a",
            new_name="fermer_a",
        ),
    ]