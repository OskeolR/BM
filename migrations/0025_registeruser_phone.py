# Generated by Django 4.1.5 on 2023-02-26 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MaleApp', '0024_orders_female_gift_orders_female_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeruser',
            name='phone',
            field=models.CharField(default='', max_length=50),
        ),
    ]
