from django.urls import path
from aviasales import views
from aviasales.apps import AviasalesConfig

app_name = AviasalesConfig.name

urlpatterns = [
    path('user_registration', views.UserRegistration.as_view(), name='user_registration'),
    path('user_detail/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('flight_info/<int:flight_pk>', views.FlightInfo.as_view(), name='flight_info')
]