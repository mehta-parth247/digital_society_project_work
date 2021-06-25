# Generated by Django 3.2.3 on 2021-05-30 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('otp', models.IntegerField(default=459)),
                ('is_activate', models.BooleanField(default=True)),
                ('is_verfied', models.BooleanField(default=False)),
                ('role', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Chairman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(blank=True, max_length=20)),
                ('contact', models.CharField(max_length=20)),
                ('profile_pic', models.FileField(default='media\\images\\default.png', upload_to='media\\images')),
                ('specialities', models.CharField(blank=True, max_length=20)),
                ('gender', models.CharField(blank=True, max_length=20)),
                ('experience', models.CharField(blank=True, max_length=20)),
                ('clinic_name', models.CharField(blank=True, max_length=30)),
                ('country', models.CharField(blank=True, max_length=30)),
                ('city', models.CharField(blank=True, max_length=30)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('aboutme', models.TextField(blank=True, max_length=500)),
                ('internship', models.CharField(blank=True, max_length=30)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secretary.user')),
            ],
        ),
    ]