from django.db import models

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
