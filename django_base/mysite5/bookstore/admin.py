from django.contrib import admin
from . import models

admin.site.register(models.Book, models.BookManager)
admin.site.register(models.Author,models.AuthorManager)
# Register your models here.
