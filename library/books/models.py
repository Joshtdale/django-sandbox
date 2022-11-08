from django.db import models
from datetime import date

class Book(models.Model):
    title = models.CharField(max_length=300)
    published_year = models.IntegerField(null=True, blank=True)
    category = models.CharField(default='Lunch', max_length=30)
    description = models.CharField(default='Its probably edible', max_length=300)
    price = models.IntegerField(null=True, blank=True)
    # author = models.CharField(max_length=30)

    def __str__(self):
        return self.title + " " + str(self.published_year)