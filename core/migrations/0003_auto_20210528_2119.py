# Generated by Django 3.2.3 on 2021-05-28 21:19

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_auto_20210517_2321"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ("-published_in",)},
        ),
        migrations.AddField(
            model_name="post",
            name="teste",
            field=models.PositiveIntegerField(
                default=2, verbose_name="Unidades"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="published_in",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2021, 5, 28, 21, 19, 33, 457191, tzinfo=utc
                )
            ),
        ),
    ]
