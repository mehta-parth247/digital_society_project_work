# Generated by Django 3.2.3 on 2021-05-30 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secretary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(blank=True, max_length=20)),
                ('contact', models.CharField(max_length=20)),
                ('profile_pic', models.FileField(default='media\\images\\pdefault.ico', upload_to='media\\images')),
                ('gender', models.CharField(blank=True, max_length=20)),
                ('country', models.CharField(blank=True, max_length=30)),
                ('city', models.CharField(blank=True, max_length=30)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('aboutme', models.TextField(blank=True, max_length=500)),
                ('age', models.CharField(max_length=20)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secretary.user')),
            ],
        ),
    ]
