import django_filters as filters
from lab3 import models


class ReaderRegistrationDateRangeFilter(filters.FilterSet):

    date = filters.DateFromToRangeFilter(field_name='registration_date')

    class Meta:
        model = models.Reader
        fields = ['date']


class BookTakenDateRangeFilter(filters.FilterSet):
    date = filters.DateFromToRangeFilter(field_name='start_date')

    class Meta:
        model = models.ReaderBookHistory
        fields = ['date']


class RoomRegistrationDateRangeFilter(filters.FilterSet):
    date = filters.DateFromToRangeFilter(field_name='start_date')

    class Meta:
        model = models.ReaderRoomHistory
        fields = ['date']


