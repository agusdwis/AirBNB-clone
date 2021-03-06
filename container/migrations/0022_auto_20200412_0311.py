# Generated by Django 3.0.5 on 2020-04-12 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('container', '0021_remove_amenities_property_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dwelling',
            name='property_id',
        ),
        migrations.AlterField(
            model_name='dwelling',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='container.Categories'),
        ),
        migrations.AlterField(
            model_name='dwelling',
            name='city_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city', to='container.Cities'),
        ),
    ]
