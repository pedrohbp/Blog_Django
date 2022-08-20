from django.db import models

from Category.models import Category

class News(models.Model):
    title = models.CharField('title', max_length=50)
    content = models.CharField('content', max_length=50)
    author = models.CharField('author', max_length=50) 

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'