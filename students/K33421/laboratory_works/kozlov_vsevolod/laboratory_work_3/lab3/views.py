from rest_framework import generics, permissions
from lab3 import serializers, models


class TestModelAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.TestModelSerializer
    queryset = models.TestModel.objects.all()
