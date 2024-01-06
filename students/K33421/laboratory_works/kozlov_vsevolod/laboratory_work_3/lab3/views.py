from rest_framework import generics, permissions, views, exceptions
from rest_framework.response import Response
from lab3 import serializers, models, filters
from django.db import models as dj_models
from scripts import create_db_data
from datetime import datetime,timedelta
from abc import abstractmethod




class ApiViewSingleObject(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        _object = self.get_object_for_get()
        serializer = self.get_serializer(_object, many=False)
        return Response(serializer.data)

    @abstractmethod
    def get_object_for_get(self):
        raise NotImplemented('You must implement get_object_for_get')



class InitDataView(views.APIView):
    def get(self, request):
        create_db_data.run()
        return Response({'date': []}, status=200)


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


class StatisticsEducationApiView(ApiViewSingleObject):
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.StatisticsEducationSerializer


    def get_object_for_get(self):
        qs = models.Reader.objects.all()
        active_qs = qs.filter(active=True)
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



class StatisticsAgeApiView(ApiViewSingleObject):
    serializer_class = serializers.StatisticsAgeSerializer

    def get_object_for_get(self):
        qs = models.Reader.objects.all()
        active_qs = qs.filter(active=True)
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


class StatisticsLibraryApiView(ApiViewSingleObject):
    serializer_class = serializers.StatisticsLibrarySerializer

    def get_object_for_get(self):
        qs_reader = filters.ReaderRegistrationDateRangeFilter(self.request.GET).qs
        new_readers = qs_reader.count()

        qs_books = filters.BookTakenDateRangeFilter(self.request.GET).qs
        books_taken = qs_books.count()
        return {'new_readers': new_readers, 'books_taken': books_taken}


class StatisticsRoomApiView(ApiViewSingleObject):
    serializer_class = serializers.StatisticsRoomSerializer
    queryset = models.Room.objects.all()

    def get_object_for_get(self):
        room_pk = self.kwargs[self.lookup_field]
        room = self.get_object()

        qs_book_taken = filters.BookTakenDateRangeFilter(
            self.request.GET
        ).qs
        qs_book_taken = qs_book_taken.filter(book_instance__room__pk=room_pk)
        books_taken = qs_book_taken.count()

        qs_reader_history = room.readers_history
        qs_reader_history = filters.RoomRegistrationDateRangeFilter(
            self.request.GET,
            queryset=qs_reader_history
        ).qs
        new_readers = qs_reader_history.count()

        return {'name': room.name, 'books_taken': books_taken, 'new_readers': new_readers}


class StatisticsRoomListApiView(StatisticsRoomApiView):
    def get(self, request, *args, **kwargs):
        room_stats = []
        for _id in models.Room.objects.values_list('id', flat=True):
            self.kwargs = {'pk': _id}
            room_stat = self.get_object_for_get()
            room_stats.append(room_stat)
        serialized = serializers.StatisticsRoomSerializer(room_stats, many=True)
        return Response(serialized.data)


class ReaderCreateApiView(generics.CreateAPIView):
    serializer_class = serializers.ReaderSerializer
    queryset = models.Reader.objects.all()


class BookInstanceRemoveApiView(generics.RetrieveDestroyAPIView):
    queryset = models.BookInstance.objects.all()
    serializer_class = serializers.BookInstanceSerializer


class BookInstanceCreateView(generics.CreateAPIView):
    serializer_class = serializers.BookInstanceCreateSerializer


class BookCreateView(generics.CreateAPIView):
    serializer_class = serializers.BookCreateSerializer


class BookInstanceListApi(generics.ListAPIView):
    serializer_class = serializers.BookInstanceSerializer
    queryset = models.BookInstance.objects.all()




class TestWarriorApi(generics.ListAPIView):
    serializer_class = serializers.TestWarriorSerializer

    def get_queryset(self):
        warriors = [{'name': 'Seva', 'race': 'dwarf'},
                    {'name': 'Koly', 'race': 'human'}]
        return warriors
