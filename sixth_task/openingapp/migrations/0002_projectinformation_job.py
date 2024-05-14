# Generated by Django 5.0.6 on 2024-05-14 16:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openingapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_description', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name': 'project_information',
                'verbose_name_plural': 'project_informations',
                'db_table': 'project_information',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('job_project_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job', to='openingapp.projectinformation')),
            ],
            options={
                'verbose_name': 'job',
                'verbose_name_plural': 'jobs',
                'db_table': 'job',
            },
        ),
    ]
