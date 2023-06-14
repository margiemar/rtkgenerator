# Generated by Django 4.2.2 on 2023-06-13 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rtk_app", "0003_alter_onetimework_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="abonreestr",
            name="dev_name",
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="abonreestr",
            name="ip_address",
            field=models.GenericIPAddressField(null=True, protocol="IPv4"),
        ),
    ]