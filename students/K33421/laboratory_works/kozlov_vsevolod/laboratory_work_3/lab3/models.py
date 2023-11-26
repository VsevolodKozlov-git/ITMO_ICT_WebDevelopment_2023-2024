from django.db import models

# Create your models here.


class TestModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
