# Generated by Django 5.0.1 on 2024-03-14 09:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("appliVanne", "0045_alter_vanne_id_positionneur"),
    ]

    operations = [
        migrations.AddField(
            model_name="revison",
            name="detail_commentaire",
            field=models.CharField(
                blank=True, default="Aucun détail", max_length=1500000, null=True
            ),
        ),
    ]
