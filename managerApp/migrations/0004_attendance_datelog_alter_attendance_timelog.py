# Generated by Django 4.0.5 on 2022-06-07 16:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managerApp', '0003_attendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='dateLog',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='timeLog',
            field=models.TimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
