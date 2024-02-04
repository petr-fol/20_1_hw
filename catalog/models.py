from django.db import models

'''
Product:
наименование,
описание,
изображение (превью),
категория,
цена за штуку,
дата создания,
дата последнего изменения.

Category:
наименование,
описание
'''


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='аватарка')
    category = models.CharField(max_length=100, verbose_name='категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='изменено')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя')
    description = models.TextField(verbose_name='описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создано')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
