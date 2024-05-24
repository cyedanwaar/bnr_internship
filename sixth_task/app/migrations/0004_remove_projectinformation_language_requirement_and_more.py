# Generated by Django 5.0.6 on 2024-05-23 12:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_projectinfoupdate_project_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectinformation',
            name='language_requirement',
        ),
        migrations.RemoveField(
            model_name='projectinformation',
            name='proposal',
        ),
        migrations.RemoveField(
            model_name='projectinformation',
            name='recruiter',
        ),
        migrations.RemoveField(
            model_name='projectinformation',
            name='security_requirement',
        ),
        migrations.RemoveField(
            model_name='projectinformation',
            name='title',
        ),
        migrations.AddField(
            model_name='opening',
            name='education',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='opening',
            name='language_requirement',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='opening',
            name='recruiter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recruiter_opening', to='mainapp.recruiter'),
        ),
        migrations.AddField(
            model_name='opening',
            name='security_requirement',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='opening',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Partner',
        ),
    ]
