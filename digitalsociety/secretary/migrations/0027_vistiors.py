# Generated by Django 3.2.3 on 2021-06-23 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secretary', '0026_suggestions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vistiors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('member_firstname', models.CharField(max_length=20)),
                ('visitor_firstname', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=20)),
                ('gender', models.CharField(blank=True, max_length=20)),
                ('currentdate', models.DateField(blank=True, null=True)),
                ('house_no', models.CharField(blank=True, max_length=200)),
                ('vechicle_deatails', models.CharField(blank=True, max_length=200)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secretary.user')),
            ],
        ),
    ]