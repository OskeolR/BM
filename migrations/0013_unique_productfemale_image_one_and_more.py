# Generated by Django 4.1.5 on 2023-02-14 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MaleApp', '0012_unique_productmale_unique_productfemale'),
    ]

    operations = [
        migrations.AddField(
            model_name='unique_productfemale',
            name='image_one',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='unique_productfemale',
            name='image_two',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='unique_productmale',
            name='image_one',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='unique_productmale',
            name='image_two',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
