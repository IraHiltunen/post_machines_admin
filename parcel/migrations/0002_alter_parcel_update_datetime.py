# Generated by Django 5.0.6 on 2024-07-06 20:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcel',
            name='update_datetime',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date published'),
        ),
    ]
