from django.db import models


class News(models.Model):
    """
    Модель новостей.
    """
    title = models.CharField('Заголовок', max_length=300, db_index=True, blank=True)
    url = models.URLField('Ссылка', max_length=300, blank=True)
    created = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        ordering = ['-created',]
        verbose_name = 'Последние новости'
        verbose_name_plural = 'Последние новости'

    def __str__(self):
        return self.title
