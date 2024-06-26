# Generated by Django 5.0.4 on 2024-05-02 12:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refapp', '0002_alter_reference_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reference',
            old_name='p_auth_address',
            new_name='project_auth_address',
        ),
        migrations.RenameField(
            model_name='reference',
            old_name='p_auth_email',
            new_name='project_auth_email',
        ),
        migrations.RenameField(
            model_name='reference',
            old_name='p_auth_fax_no',
            new_name='project_auth_fax_no',
        ),
        migrations.RenameField(
            model_name='reference',
            old_name='p_auth_name',
            new_name='project_auth_name',
        ),
        migrations.RenameField(
            model_name='reference',
            old_name='p_auth_phone_no',
            new_name='project_auth_phone_no',
        ),
        migrations.RenameField(
            model_name='reference',
            old_name='t_auth_address',
            new_name='technical_auth_address',
        ),
        migrations.RenameField(
            model_name='reference',
            old_name='t_auth_email',
            new_name='technical_auth_email',
        ),
        migrations.RenameField(
            model_name='reference',
            old_name='t_auth_fax_no',
            new_name='technical_auth_fax_no',
        ),
        migrations.RenameField(
            model_name='reference',
            old_name='t_auth_name',
            new_name='technical_auth_name',
        ),
        migrations.RenameField(
            model_name='reference',
            old_name='t_auth_phone_no',
            new_name='technical_auth_phone_no',
        ),
        migrations.AddField(
            model_name='reference',
            name='cost',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reference',
            name='currency',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='reference',
            name='description',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='reference',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reference',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='currency',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='BidderSupplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='refapp.organization')),
                ('partner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partner', to='refapp.organization')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityDeliverable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_title', models.CharField(blank=True, max_length=255, null=True)),
                ('activity_description', models.TextField(blank=True, max_length=2000, null=True)),
                ('activity_bidder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity', to='refapp.biddersupplier')),
            ],
        ),
        migrations.AddField(
            model_name='resource',
            name='resource_bidder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resource', to='refapp.biddersupplier'),
        ),
        migrations.DeleteModel(
            name='BiderSupplier',
        ),
    ]
