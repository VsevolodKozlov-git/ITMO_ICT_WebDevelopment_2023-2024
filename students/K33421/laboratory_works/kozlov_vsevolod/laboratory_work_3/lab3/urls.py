from django.urls import path
from lab3 import views

app_name = 'lab3'

urlpatterns = [
    path('test_api_view/', views.TestModelAPIView.as_view(), name='test_api_view'),
    path('add_model_data/', views.InitDataView.as_view()),
    path('reader/books/<int:reader_pk>', views.ReaderBooksApiView.as_view(), name='reader_books'),
    path('reader/outdated', views.OutdatedReadersApiView.as_view(), name='reader_outdated'),
    path('reader/rare_books', views.ReaderRareBook.as_view(), name='reader_rare_books'),
    path('reader/book_month_ago', views.ReaderBookMonthAgoApi.as_view(), name='reader_book_month_age'),
    path('reader/new', views.ReaderNewApiView.as_view(), name='reader_new'),
    path('statistics/education', views.StatisticsEducationApiView.as_view(), name='statistics_education'),
    path('statistics/age', views.StatisticsAgeApiView.as_view(), name='statistice_age'),
    path('book_instance/remove/<int:pk>', views.BookInstanceRemoveApiView.as_view(), name='book_instance_remove'),
    path('book_instance/create', views.BookInstanceCreateView.as_view(), name='book_instance_create')
]
