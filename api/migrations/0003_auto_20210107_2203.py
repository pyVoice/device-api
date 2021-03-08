# Generated by Django 3.0.5 on 2021-01-07 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_device_operating_system"),
    ]

    operations = [
        migrations.AddField(
            model_name="device",
            name="location",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="device",
            name="operating_system",
            field=models.CharField(max_length=50),
        ),
    ]
