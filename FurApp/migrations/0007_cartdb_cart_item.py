# Generated by Django 5.1 on 2024-11-20 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FurApp', '0006_orderdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdb',
            name='cart_item',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]