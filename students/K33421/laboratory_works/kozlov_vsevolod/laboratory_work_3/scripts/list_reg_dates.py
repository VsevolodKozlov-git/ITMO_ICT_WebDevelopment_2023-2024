from lab3 import models
from django.db import models as dj_models
from datetime import datetime, timedelta


def q_exp():


    title_Q0 = dj_models.Q(title='BookTitle0')
    title_Q1 = dj_models.Q(title='BookTitle0')
    rare_or_title = models.Book.objects.filter(
        title_Q0 | title_Q1
    )
    print(rare_or_title)


models.ReaderBookHistory.objects.filter(start_date=dj_models.F('end_date'))


def run():
    print(models.ReaderBookHistory.objects.filter(start_date=dj_models.F('end_date')))

