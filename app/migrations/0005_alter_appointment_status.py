# Generated by Django 5.1.2 on 2025-01-30 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_appointment_date_time_appointment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(auto_created=True, choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed')], default='Scheduled', max_length=20),
        ),
    ]
