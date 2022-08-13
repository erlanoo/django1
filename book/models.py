from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=1)
    type = models.CharField(max_length=255)
    avialable = models.BooleanField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = "Продукты"

class Pricing(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    full_support = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    storage = models.CharField(max_length=50)
    price = models.PositiveIntegerField(default=50)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Название'



