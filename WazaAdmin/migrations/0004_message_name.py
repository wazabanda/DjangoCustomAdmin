# Generated by Django 4.2.3 on 2023-07-21 07:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("WazaAdmin", "0003_message"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="name",
            field=models.CharField(default="", max_length=30),
        ),
    ]
