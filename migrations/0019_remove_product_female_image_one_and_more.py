# Generated by Django 4.1.5 on 2023-02-16 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MaleApp', '0018_product_female_image_one_product_female_image_two'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_female',
            name='image_one',
        ),
        migrations.RemoveField(
            model_name='product_female',
            name='image_two',
        ),
        migrations.AddField(
            model_name='product',
            name='number_click',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='product_female',
            name='number_click',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
