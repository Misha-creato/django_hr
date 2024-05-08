from django.db import models


LOGO_SIZE = (100, 100)


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
    hidden = models.BooleanField(
        verbose_name='Скрыта',
        default=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'companies'
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Vacancy(models.Model):
    EXPERIENCE_CHOICES = (
        ('0_', 'Не имеет значения',),
        ('1_3', 'От 1 до 3 лет',),
        ('3_6', 'От 3 до 6 лет',),
        ('6_', 'От 6 лет',),
    )
    EMPLOYMENT_CHOICES = (
        ('full', 'Полная занятость',),
        ('part', 'Частичная занятость',),
        ('probation', 'Стажировка',),
    )
    SCHEDULE_CHOICES = (
        ('full_day', 'Полный день',),
        ('shift', 'Сменный график',),
        ('flexible', 'Гибкий график',),
        ('remote', 'Удаленная работа',),
        ('fly_in_fly_out', 'Вахтовый метод',),
    )
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
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

