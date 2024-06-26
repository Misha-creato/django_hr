import io

from PIL import Image

from solo.models import SingletonModel

from django.db import models
from django.core.files.uploadedfile import SimpleUploadedFile

from utils.constants import (
    EXPERIENCE_CHOICES,
    EMPLOYMENT_CHOICES,
    SCHEDULE_CHOICES,
)


LOGO_SIZE_WIDTH = 100
LOGO_SIZE_HEIGHT = 100


class Company(models.Model):
    name = models.CharField(
        verbose_name='Наименование',
        max_length=256,
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    logo = models.ImageField(
        verbose_name='Лого',
        upload_to='logos',
        null=True,
        blank=True,
    )
    thumbnail = models.ImageField(
        verbose_name='Миниатюра',
        upload_to='thumbnails',
        null=True,
        blank=True,
    )
    hidden = models.BooleanField(
        verbose_name='Скрыта',
        default=False,
    )

    def __str__(self):
        return self.name

    def __make_thumbnail(self):
        with Image.open(self.logo) as img:
            if img.mode in ('RGBA', 'LA'):
                img = img.convert('RGB')

            img.thumbnail((LOGO_SIZE_WIDTH, LOGO_SIZE_HEIGHT))
            thumb = io.BytesIO()
            img.save(thumb, format='JPEG', quality=90)

            self.thumbnail = SimpleUploadedFile(self.logo.name, thumb.getvalue())

    def save(self, *args, **kwargs):
        if self.logo:
            if self.pk:
                old_logo = Company.objects.get(pk=self.pk).logo
                if self.logo != old_logo:
                    self.__make_thumbnail()
            else:
                self.__make_thumbnail()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'companies'
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Vacancy(models.Model):
    company = models.ForeignKey(
        verbose_name='Компания',
        to=Company,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        verbose_name='Должность',
        max_length=256,
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    salary = models.CharField(
        verbose_name='Заработная плата',
        max_length=256,
        default='Не указана',
    )
    experience = models.CharField(
        verbose_name='Опыт работы',
        max_length=64,
        choices=EXPERIENCE_CHOICES,
    )
    employment = models.CharField(
        verbose_name='Тип занятости',
        max_length=64,
        choices=EMPLOYMENT_CHOICES,
    )
    schedule = models.CharField(
        verbose_name='График работы',
        max_length=64,
        choices=SCHEDULE_CHOICES,
    )
    hidden = models.BooleanField(
        verbose_name='Скрыта',
        default=False,
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'vacancies'
        ordering = ['-created_at']
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'


def resume_directory_path(instance, filename):
    return f'resumes/{instance.vacancy.company.name}/{instance.vacancy.title}/{filename}'


class VacancyResponse(models.Model):
    vacancy = models.ForeignKey(
        verbose_name='Вакансия',
        to=Vacancy,
        on_delete=models.CASCADE,
    )
    email = models.EmailField(
        verbose_name='Адрес электронной почты',
    )
    resume = models.FileField(
        verbose_name='Резюме',
        upload_to=resume_directory_path,
    )
    covering_letter = models.TextField(
        verbose_name='Сопроводительное письмо',
        null=True,
        blank=True,
    )
    viewed = models.BooleanField(
        verbose_name='Просмотрено',
        default=False,
    )
    created_at = models.DateTimeField(
        verbose_name='Время создания',
        auto_now_add=True,
    )

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'vacancy_responses'
        verbose_name = 'Отлик'
        verbose_name_plural = 'Отлики'


class Header(SingletonModel):
    singleton_instance_id = 2
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=256,
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='headers',
        help_text="Пожалуйста, загрузите изображение в формате JPG, PNG",
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'header'
        verbose_name = 'Шапка'
