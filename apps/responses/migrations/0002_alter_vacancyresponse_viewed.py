# Generated by Django 4.2 on 2024-05-08 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('responses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancyresponse',
            name='viewed',
            field=models.BooleanField(default=False, verbose_name='Просмотрено'),
        ),
    ]
