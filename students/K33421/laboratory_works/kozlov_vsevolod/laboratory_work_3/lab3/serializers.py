from rest_framework import serializers
from lab3 import models


class TestModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TestModel
        fields = '__all__'


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


class BookInstanceSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=False)

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