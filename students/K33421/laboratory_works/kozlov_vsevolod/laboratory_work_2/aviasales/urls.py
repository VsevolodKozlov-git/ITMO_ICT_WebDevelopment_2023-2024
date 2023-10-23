from django.urls import path
from aviasales import views

appname='aviasales'

urlpatterns = [
    path('hello', views.hello_view, name='hello')
]