# Generated by Django 3.0.5 on 2020-04-12 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('container', '0017_remove_amenities_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.SmallIntegerField(default=1)),
            ],
        ),
    ]
