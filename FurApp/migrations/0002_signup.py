# Generated by Django 5.1.2 on 2024-10-26 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FurApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_up', models.CharField(blank=True, max_length=100, null=True)),
                ('Email_up', models.CharField(blank=True, max_length=100, null=True)),
                ('Number_up', models.IntegerField(blank=True, null=True)),
                ('Password', models.CharField(blank=True, max_length=100, null=True)),
                ('Confirm', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
