# Generated by Django 5.1.2 on 2024-11-16 13:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100)),
                ('service_description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='PetProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.CharField(max_length=50)),
                ('breed', models.CharField(max_length=50)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('vaccination_status', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='PetRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_time', models.DateTimeField(auto_now_add=True)),
                ('check_out_time', models.DateTimeField(blank=True, null=True)),
                ('daily_activities', models.TextField(blank=True, null=True)),
                ('health_notes', models.TextField(blank=True, null=True)),
                ('emergency_contact', models.CharField(blank=True, max_length=100, null=True)),
                ('vaccination_status', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.userprofile')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.petprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Canceled', 'Canceled')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.userprofile')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.petprofile')),
                ('services', models.ManyToManyField(to='app.services')),
            ],
        ),
    ]
