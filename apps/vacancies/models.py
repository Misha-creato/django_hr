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
