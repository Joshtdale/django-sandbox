from django.db import models
from datetime import date

class Book(models.Model):
    title = models.CharField(max_length=300)
    year = models.DateField(default=date.today)
    # author = models.CharField(max_length=30)