# Generated by Django 4.2 on 2024-05-08 10:34

from django.db import migrations, models
import django.db.models.deletion
import responses.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vacancies', '0002_alter_company_logo_vacancy'),
    ]

    operations = [
        migrations.CreateModel(
            name='VacancyResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Адрес электронной почты')),
                ('resume', models.FileField(upload_to=responses.models.resume_directory_path, verbose_name='Резюме')),
                ('covering_letter', models.TextField(blank=True, null=True, verbose_name='Сопроводительное письмо')),
                ('viewed', models.BooleanField(default=False, verbose_name='Просмотрена')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancies.vacancy', verbose_name='Вакансия')),
            ],
            options={
                'verbose_name': 'Отлик',
                'verbose_name_plural': 'Отлики',
                'db_table': 'vacancy_responses',
            },
        ),
    ]