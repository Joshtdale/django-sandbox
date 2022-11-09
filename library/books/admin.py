from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    fields = ('title', 'category', 'description', 'published_year', 'price', 'cuisine')
admin.site.register(Book, BookAdmin)