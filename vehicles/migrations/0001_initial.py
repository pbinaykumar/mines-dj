# Generated by Django 5.0.1 on 2024-01-03 10:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicle_tag_id', models.CharField(max_length=21, primary_key=True, serialize=False)),
                ('vehicle_number', models.CharField(max_length=21)),
                ('vehicle_name', models.CharField(max_length=51)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('1', 'Talcher Mines'), ('2', 'Jharkhand Mines'), ('3', 'Parked'), ('4', 'Weighted'), ('5', 'Dumped')], max_length=21)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle')),
            ],
        ),
    ]
