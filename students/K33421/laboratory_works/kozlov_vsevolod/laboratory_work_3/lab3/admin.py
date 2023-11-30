from django.contrib import admin
from lab3 import models

# Register your models here.
model_classes = [models.Publisher, models.Section, models.Book,
                 models.Author, models.BookAuthors,
                 models.BookInstance, models.Room,
                 models.ReaderBookHistory, models.ReaderRoomHistory,
                 models.Reader]
admin.site.register(models.TestModel)
