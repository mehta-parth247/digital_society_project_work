# Generated by Django 3.2.3 on 2021-06-01 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secretary', '0004_chairman_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chairman',
            name='profile_pic',
        ),
    ]