# Generated by Django 4.2 on 2024-05-10 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails', verbose_name='Миниатюра'),
        ),
    ]