from django.db import models

class Article(models.Model):
    article_title = models.CharField('Название статьи', max_length=100)
    article_text = models.TextField('Текст статьи', max_length=2000)

    def __str__(self):
        return str(self.article_title)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'






