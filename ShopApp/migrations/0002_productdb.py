# Generated by Django 5.1.2 on 2024-10-15 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='productdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Category', models.CharField(blank=True, max_length=100, null=True)),
                ('Product_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Quantity', models.IntegerField(blank=True, null=True)),
                ('MRP', models.IntegerField(blank=True, null=True)),
                ('Description', models.TextField(blank=True, max_length=100, null=True)),
                ('Country_Of_Orgin', models.CharField(blank=True, max_length=100, null=True)),
                ('Manufactured_By', models.CharField(blank=True, max_length=100, null=True)),
                ('Image1', models.ImageField(blank=True, null=True, upload_to='proimg')),
                ('Image2', models.ImageField(blank=True, null=True, upload_to='proimg')),
                ('Image3', models.ImageField(blank=True, null=True, upload_to='proimg')),
            ],
        ),
    ]