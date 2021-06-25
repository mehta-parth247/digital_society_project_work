# Generated by Django 3.2.3 on 2021-06-10 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('secretary', '0009_auto_20210607_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watchman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(blank=True, max_length=20)),
                ('contact', models.CharField(max_length=20)),
                ('profile_pic', models.FileField(default='media\\images\\default.png', upload_to='media\\images')),
                ('gender', models.CharField(blank=True, max_length=20)),
                ('age', models.CharField(blank=True, max_length=20)),
                ('state', models.CharField(blank=True, max_length=30)),
                ('country', models.CharField(blank=True, max_length=30)),
                ('city', models.CharField(blank=True, max_length=30)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('aboutme', models.TextField(blank=True, max_length=500)),
                ('work', models.CharField(blank=True, max_length=20)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secretary.user')),
            ],
        ),
        migrations.CreateModel(
            name='ClientRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('chairman_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secretary.chairman')),
                ('watchman_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.watchman')),
            ],
        ),
    ]