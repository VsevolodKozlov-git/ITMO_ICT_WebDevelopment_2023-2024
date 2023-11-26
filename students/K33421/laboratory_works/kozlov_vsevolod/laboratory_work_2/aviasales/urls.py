from django.urls import path

from aviasales import views
from aviasales.apps import AviasalesConfig

app_name = AviasalesConfig.name

urlpatterns = [
    path('', views.MainPage.as_view(), name='root'),
    path('user_registration', views.UserRegistration.as_view(), name='user_registration'),
    path('user_detail/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('flight_info/<int:flight_pk>', views.FlightInfo.as_view(), name='flight_info'),
    path('auth_test', views.auth_test, name='auth_test'),
    path('my_flights', views.MyFlights.as_view(), name='my_flights'),
    path('userflight_update/<int:pk>', views.UserFlightUpdateView.as_view(), name='userflight_update'),
    path('userflight_delete/<int:pk>', views.UserFlightDeleteView.as_view(), name='userflight_delete'),
    path('review_create', views.ReviewCreateView.as_view(), name='review_create'),
    path('userflight_reservation_list', views.UserFlightsReservationList.as_view(), name='userflight_reservation_list'),
    path(r'userflight_reservation_form/<int:flight_pk>', views.UserFlightsReservationForm.as_view(),
         name='userflight_reservation_form'),
    path('flight_review_select', views.FlightReviewSelect.as_view(), name='flight_review_select'),
    path('flight_review_list/<int:flight_pk>', views.FlightReviewList.as_view(), name='flight_review_list')
]
