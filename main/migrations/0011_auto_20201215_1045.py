# Generated by Django 3.1.2 on 2020-12-15 07:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20201213_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gap',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='lateness',
            name='time_of_lateness',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='notification',
            name='gap',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.gap'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='lateness',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.lateness'),
        ),
    ]
