# Generated by Django 3.0.5 on 2021-01-08 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0007_auto_20210107_2215"),
    ]

    operations = [
        migrations.AddField(
            model_name="device",
            name="device_id",
            field=models.CharField(default="", max_length=25),
        ),
    ]
