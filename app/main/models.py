from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    tag = models.CharField(max_length=100, verbose_name='Метка', default='main_menu')
    level = models.PositiveIntegerField(default=1, verbose_name='Уровень')
    url = models.CharField(max_length=255, verbose_name='Ссылка')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('level',)
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
