# Generated by Django 5.0 on 2024-04-05 11:18

import home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to=home.models.upload_to),
        ),
    ]
