from django.db import models
from datetime import date

class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Cuisine(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=300)
    published_year = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, default=None)
    cuisine = models.ForeignKey('Cuisine', on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(default='Its probably edible', max_length=300)
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title + " " + str(self.published_year)

