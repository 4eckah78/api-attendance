# Generated by Django 3.1.2 on 2020-11-09 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20201108_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='table_name',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]
