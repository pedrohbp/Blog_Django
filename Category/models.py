from django.db import models

class Category(models.Model):
    name = models.CharField('name', max_length=50)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'