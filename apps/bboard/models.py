from django.db import models
from django.utils.translation import gettext


class Board(models.Model):
    class Types(models.TextChoices):
        BUY = 'B', gettext("Куплю")
        SELL = 'S', gettext("Продам")

    title = models.CharField(max_length=50, verbose_name='Тип товара')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    type = models.CharField(max_length=1, choices=Types.choices, default=Types.SELL, verbose_name='Тип обьявление')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name = 'Обьявление'
        verbose_name_plural = 'Обьявлении'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
        ordering = ['name']
