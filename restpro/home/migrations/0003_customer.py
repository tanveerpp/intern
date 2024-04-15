# Generated by Django 5.0 on 2024-04-08 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_student_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=20)),
                ('cemail', models.EmailField(max_length=254)),
                ('mob', models.IntegerField()),
                ('product', models.CharField(max_length=30)),
            ],
        ),
    ]
