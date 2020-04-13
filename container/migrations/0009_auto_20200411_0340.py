# Generated by Django 3.0.5 on 2020-04-11 03:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('container', '0008_auto_20200410_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='dwelling',
            name='publis',
            field=models.DateField(default=datetime.datetime(2020, 4, 11, 3, 40, 57, 954463, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dwelling',
            name='city_id',
            field=models.IntegerField(default=1),
        ),
    ]
