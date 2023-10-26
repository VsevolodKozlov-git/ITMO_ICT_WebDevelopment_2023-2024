from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth import get_user_model
from aviasales import models, forms
from aviasales.apps import AviasalesConfig
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse

appname = AviasalesConfig.name
# Create your views here.

user_model = get_user_model()

def get_template_path(name):
    return f'{appname}/{name}.html'


class UserRegistration(View):
    template_path = get_template_path('user_registration')
    form_class = forms.UserRegisterForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_path, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(user.get_absolute_url())
        context = {'form': form}
        return render(request, self.template_path, context)


class UserDetail(DetailView):
    model = user_model
    template_name = 'aviasales/user_detail.html'

    def get_queryset(self):
        return super().get_queryset()


class FlightInfo(View):
    template_path = get_template_path('flight_info')

    def get(self, request, flight_pk):
        # todo  userflight__approved=True
        user_flights = models.UserFlight.objects.filter(flight__pk=flight_pk)
        context = {'user_flights': user_flights}
        return render(request, self.template_path, context=context)


class MyFlights(LoginRequiredMixin, View):

    template_path = get_template_path('my_flights')

    def get(self, request):
        user = request.user
        # todo  userflight__approved=True
        user_flights = models.UserFlight.objects.filter(user__pk=user.pk)
        context = {'user_flights': user_flights}
        return render(request, self.template_path, context)


class UserFlightUpdateView(UserPassesTestMixin, UpdateView):
    model = models.UserFlight
    fields = ['seat_number']
    success_url = reverse_lazy('aviasales:my_flights')
    def test_func(self):
        userflight_url_pk = self.kwargs[self.pk_url_kwarg]
        user = self.request.user
        try:
            # todo  userflight__approved=True
            user.userflight_set.get(pk=userflight_url_pk)
            return True
        except models.UserFlight.DoesNotExist:
            return False


class UserFlightDeleteView(UserPassesTestMixin, DeleteView):
    model = models.UserFlight
    success_url = reverse_lazy('aviasales:my_flights')

    def test_func(self):
        userflight_url_pk = self.kwargs[self.pk_url_kwarg]
        user = self.request.user
        try:
            # todo  userflight__approved=True
            user.userflight_set.get(pk=userflight_url_pk)
            return True
        except models.UserFlight.DoesNotExist:
            return False


class UserRegistration(View):
    template_path = get_template_path('user_registration')
    form_class = forms.UserRegisterForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_path, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(user.get_absolute_url())
        context = {'form': form}
        return render(request, self.template_path, context)


class ReviewCreateView(LoginRequiredMixin, View):
    template_path = get_template_path('review_form')
    form_class = forms.ReviewForm

    def get(self, request, *args, **kwargs):
        user = request.user
        form = self.form_class(user)
        context = {'form': form}
        return render(request, self.template_path, context)

    def post(self, request, *args, **kwargs):
        user = request.user
        form = self.form_class(user, request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('aviasales:review_create'))
        context = {'form': form}
        return render(request, self.template_path, context)


class ReviewListView(ListView):
    model = models.Review


class UserFlightsReservationList(LoginRequiredMixin, ListView):
    model = models.Flight
    template_name = get_template_path('userflight_reservation_list')

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        reserved_flights_pks = {i.flight.pk for i in user.userflight_set.get_queryset()}
        queryset = queryset.exclude(pk__in=reserved_flights_pks)
        return queryset


class UserFlightsReservationForm(LoginRequiredMixin, View):

    template_path = get_template_path('userflight_reservation_form')
    form_class = forms.ReservationForm

    last_get_flight = None

    def get(self, request, flight_pk, *args, **kwargs):
        user = request.user
        flight = models.Flight.objects.get(pk=flight_pk)
        self.last_get_flight = flight
        form = self.form_class(user, flight)
        context = {'form': form}
        return render(request, self.template_path, context)

    def post(self, request, flight_pk, *args, **kwargs):
        user = request.user
        flight = models.Flight.objects.get(pk=flight_pk)
        form = self.form_class(user, flight, request.POST)
        if form.is_valid():
            form.save()
            # todo сделать redirect на страницу с бронированием
            return redirect(reverse('not ready'))
        context = {'form': form}
        return render(request, self.template_path, context)


@login_required()
def auth_test(request):
    user = request.user
    return HttpResponse(f'Hello {user.get_username()}')
