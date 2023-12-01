# Ошибка django ORM


```python
book_cnt = models.Book.objects.annotate(
        instances_cnt=dj_models.Count('instances')
    )
rare_books = book_cnt.filter(instances_cnt__lte=2)
rare_books_instances = rare_books.values_list('instances', flat=True)
```



Просто значения поля работают хорошо
```python
book_cnt = models.Book.objects.annotate(
        instances_cnt=dj_models.Count('instances')
    )
rare_books = book_cnt.filter(instances_cnt__lte=2)
books_id = set(rare_books.values_list('id', flat=True))
print(books_id)
```


Prefetch не помог
```python
rare_books = book_cnt.prefetch_related('instances').filter(instances_cnt__lte=2)
print(rare_books.values_list('instances', flat=True))
```

При этом без annotate values_list работает отлично
```python
inst = models.Book.objects.filter(year__gte=2020).values_list('instances')
print(len(inst))
```
