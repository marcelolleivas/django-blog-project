# Generated by Django 3.2.3 on 2021-05-29 01:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_in',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 29, 1, 10, 2, 179238, tzinfo=utc)),
        ),
    ]
