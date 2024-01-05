# Serializers
```python
from lab3 import models
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        exclude = ['id']

class BookSerializer(serializers.ModelSerializer):
    section = serializers.StringRelatedField(read_only=True)
    publisher = serializers.StringRelatedField(read_only=True)
    authors = AuthorSerializer(many=True)

    class Meta:
        model = models.Book
        exclude = ['rooms', 'id']


class BookCreateSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=models.Author.objects.all()
    )
    class Meta:
        model = models.Book
        exclude = ['rooms', 'id']


class BookInstanceSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=False)

    class Meta:
        model = models.BookInstance
        exclude = ['id']


class BookInstanceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BookInstance
        exclude = ['id']


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reader
        exclude = ['education', 'rooms', 'book_instances']


class StatisticsEducationSerializer(serializers.Serializer):
    degree = serializers.FloatField()
    higher = serializers.FloatField()
    middle = serializers.FloatField()
    beginner = serializers.FloatField()


class StatisticsAgeSerializer(serializers.Serializer):
    under_20 = serializers.FloatField()
    after_20 = serializers.FloatField()


class StatisticsSerializer(serializers.Serializer):
    books_taken = serializers.IntegerField()
    new_readers = serializers.IntegerField()
```