# Generated by Django 5.0.1 on 2024-03-06 10:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("appliVanne", "0034_rename_id_revison_vanne_revison_id_revision_vanne"),
    ]

    operations = [
        migrations.RenameField(
            model_name="revison",
            old_name="id_revison",
            new_name="id_revision",
        ),
    ]
