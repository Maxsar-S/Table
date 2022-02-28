from django.db import models


class Cell(models.Model):
    date = models.DateField(blank=False)
    name = models.CharField(blank=False, max_length=128)
    quantity = models.IntegerField(blank=False)
    distance = models.DecimalField(blank=False, decimal_places=2, max_digits=12)

    def __str__(self):
        return f'{self.name}'
