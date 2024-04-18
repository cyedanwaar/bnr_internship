# Generated by Django 5.0.4 on 2024-04-18 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8)),
            ],
        ),
    ]
