from rest_framework import generics, permissions, views, exceptions
from rest_framework.response import Response
from lab3 import serializers, models
from django.db import models as dj_models
from scripts import create_db_data
from datetime import datetime,timedelta

class InitDataView(views.APIView):
    def get(self, request):
        create_db_data.run()
        return Response({'date': []}, status=200)


class TestModelAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.TestModelSerializer
    queryset = models.TestModel.objects.all()


class ReaderBooksApiView(generics.ListAPIView):
    serializer_class = serializers.BookInstanceSerializer

    def get_queryset(self):
        reader_pk = self.kwargs.get('reader_pk', None)
        if reader_pk is None:
            raise exceptions.ValidationError('Specify reader_pk in url')

        reader_books_qs = models.ReaderBookHistory.objects.filter(reader_id=reader_pk,
                                                end_date__isnull=True)
        # todo values list вовзращает все. Переписать
        instances_id = set(reader_books_qs.values_list('book_instance', flat=True))
        instances = models.BookInstance.objects.filter(id__in=instances_id)
        return instances


class OutdatedReadersApiView(generics.ListAPIView):
    serializer_class = serializers.ReaderSerializer

    def get_queryset(self):
        year_ago = datetime.now() - timedelta(days=365)
        outdated_qs = models.Reader.objects.filter(registration_date__lt=year_ago,
                                                   active=True)
        return outdated_qs


class ReaderRareBook(generics.ListAPIView):
    serializer_class = serializers.ReaderSerializer

    def get_queryset(self):
        book_cnt = models.Book.objects.annotate(
            instances_cnt=dj_models.Count('instances')
        )
        rare_books_qs = book_cnt.filter(instances_cnt__lte=2)
        rare_books_id = set(rare_books_qs.values_list('id', flat=True))
        rare_inst_qs = models.BookInstance.objects.filter(book_id__in=rare_books_id)
        rare_reader_ids = set(rare_inst_qs.values_list('readers', flat=True))
        rare_readers = models.Reader.objects.filter(id__in=rare_reader_ids)
        return rare_readers

class ReaderBookMonthAgoApi(generics.ListAPIView):
    serializer_class = serializers.ReaderSerializer

    def get_queryset(self):
        month_ago = datetime.now() - timedelta(days=30)

        reader_history = models.ReaderBookHistory.objects.filter(
            start_date__lt=month_ago,
            end_date__isnull=True
        )
        reader_ids = set(reader_history.values_list('reader', flat=True))
        readers = models.Reader.objects.filter(id__in=reader_ids)
        return readers

class StatisticsEducationApiView(views.APIView):
    serializer_class = serializers.StatisticsEducationSerializer

    def get(self, request):
        qs = self.get_queryset()
        qs_serialized = self.serializer_class(qs, many=False)
        return Response(qs_serialized.data, status=200)

    def get_queryset(self):
        active_qs = models.Reader.objects.filter(active=True)
        active_users = len(active_qs)
        edu_stat_list = active_qs.values('education').annotate(cnt=dj_models.Count('id'))
        edu_code_to_title = dict(models.Reader.education_types)
        res = {}
        for edu_stat in edu_stat_list:
            edu_code = edu_stat['education']
            cnt = edu_stat['cnt']
            edu_title = edu_code_to_title[edu_code]
            res[edu_title] = round(cnt / active_users, 3)
        return res


class StatisticsAgeApiView(views.APIView):
    serializer_class = serializers.StatisticsAgeSerializer

    def get(self, request):
        qs = self.get_queryset()
        qs_serialized = self.serializer_class(qs, many=False)
        return Response(qs_serialized.data, status=200)

    def get_queryset(self):
        active_qs = models.Reader.objects.filter(active=True)
        active_users = len(active_qs)
        n = datetime.now()
        birthdate_18 = datetime(year=n.year - 20, month=n.month, day=n.day)

        age_stat = active_qs.aggregate(
            under_20=dj_models.Count(
                'id',
                filter=dj_models.Q(birth_date__gt=birthdate_18)
            ),
            after_20=dj_models.Count(
                'id',
                filter=dj_models.Q(birth_date__lte=birthdate_18)
            ))
        for k, v in age_stat.items():
            age_stat[k] = round(v / active_users, 3)
        return age_stat


class ReaderNewApiView(generics.CreateAPIView):
    serializer_class = serializers.ReaderSerializer
    queryset = models.Reader.objects.all()


class BookInstanceRemoveApiView(generics.RetrieveDestroyAPIView):
    queryset = models.BookInstance.objects.all()
    serializer_class = serializers.BookInstanceSerializer


class BookInstanceCreateView(generics.CreateAPIView):
    serializer_class = serializers.BookInstanceSerializer


# class BookCreateView(generics.CreateAPIView):
#     serializer_class =


