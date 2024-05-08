from django.db import models


class Header(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=256,
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='headers'
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'headers'
        verbose_name = 'Шапка'
        verbose_name_plural = 'Шапки'
