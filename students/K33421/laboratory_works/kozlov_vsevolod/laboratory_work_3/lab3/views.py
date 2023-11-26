from rest_framework import generics
from lab3 import serializers, models


class TestModelAPIView(generics.ListAPIView):
    serializer_class = serializers.TestModelSerializer
    queryset = models.TestModel.objects.all()
