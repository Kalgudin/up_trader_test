from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    level = models.PositiveIntegerField(default=1, verbose_name='Уровень')
    url = models.CharField(max_length=255, verbose_name='Ссылка')

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('level',)
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
