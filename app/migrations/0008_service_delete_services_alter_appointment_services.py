# Generated by Django 5.1.2 on 2024-11-16 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_daily_activities_petrecord_activities_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100)),
                ('service_description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Services',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='services',
            field=models.ManyToManyField(to='app.service'),
        ),
    ]