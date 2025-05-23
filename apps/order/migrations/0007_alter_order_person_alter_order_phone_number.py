# Generated by Django 5.2 on 2025-05-07 08:14

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_order_child'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='person',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=20, region=None),
        ),
    ]
