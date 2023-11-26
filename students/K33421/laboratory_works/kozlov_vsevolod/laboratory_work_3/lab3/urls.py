from django.urls import path
from lab3 import views

app_name = 'lab3'

urlpatterns = [
    path('test_api_view/', views.TestModelAPIView.as_view(), name='test_api_view'),
]
