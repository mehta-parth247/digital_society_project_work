# Generated by Django 3.2.3 on 2021-06-01 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretary', '0003_auto_20210601_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='chairman',
            name='state',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
