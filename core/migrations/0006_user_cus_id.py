# Generated by Django 4.1.7 on 2023-04-01 07:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0005_usersettings_app_updates_usersettings_biometric_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="cus_id",
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]
