# Generated by Django 5.2 on 2025-04-13 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0003_country_continent_destination_continent'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='period',
            field=models.IntegerField(blank=True, default=10, null=True),
        ),
    ]
