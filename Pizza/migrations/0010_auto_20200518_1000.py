# Generated by Django 3.0.5 on 2020-05-18 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pizza', '0009_auto_20200511_1631'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cadconsumidor',
            old_name='author',
            new_name='user',
        ),
    ]
