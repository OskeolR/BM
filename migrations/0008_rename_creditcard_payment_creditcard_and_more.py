# Generated by Django 4.1.5 on 2023-02-06 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MaleApp', '0007_rename_sub_subscribe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='Creditcard',
            new_name='creditcard',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='Cvc',
            new_name='cvc',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='Exp',
            new_name='exp',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='Fullname',
            new_name='fullname',
        ),
    ]