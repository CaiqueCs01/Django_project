# Generated by Django 3.0.5 on 2020-04-14 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('senha', models.CharField(max_length=12)),
                ('tipo', models.CharField(max_length=10)),
            ],
        ),
    ]