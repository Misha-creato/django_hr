from django.db import models

from vacancies.models import Vacancy


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
