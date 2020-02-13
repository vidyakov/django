from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Назвние', unique=True, max_length=60)
    description = models.TextField(verbose_name='Описание', blank=True)
    href = models.CharField(verbose_name='Ссылка', unique=True, max_length=10, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название', unique=True, max_length=60)
    short_description = models.TextField(verbose_name='Краткое описание', max_length=128)
    description = models.TextField(verbose_name='Описание', blank=True)
    image = models.ImageField(upload_to='products_imgs', blank=True, verbose_name='Фото')
    price = models.DecimalField(null=True, verbose_name='Цена', max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(null=True, verbose_name='Количество')

    def __str__(self):
        return f'{self.name} {self.category.name}'


class Contacts(models.Model):
    city = models.CharField(verbose_name='Город', max_length=30)
    phone = models.CharField(verbose_name='Телефон (формат: +7-888-888-8888)', max_length=15)
    email = models.CharField(verbose_name='Почта', max_length=64)
    address = models.CharField(verbose_name='Адрес', max_length=64)
