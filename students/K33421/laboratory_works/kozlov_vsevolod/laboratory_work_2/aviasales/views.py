from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import DetailView, UpdateView, DeleteView, ListView

from aviasales import models, forms
from aviasales.apps import AviasalesConfig

appname = AviasalesConfig.name
# Create your views here.

user_model = get_user_model()


def get_template_path(name):
    return f'{appname}/{name}.html'


class MainPage(View):
    template_path = get_template_path('root')

    def get(self, request):
        return render(request, self.template_path)


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


class FlightInfo(View):
    template_path = get_template_path('flight_info')

    def get(self, request, flight_pk):
        user_flights = models.UserFlight.objects.filter(flight__pk=flight_pk,
                                                        approved=True)
        context = {'user_flights': user_flights}
        return render(request, self.template_path, context=context)


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

    def get(self, request, flight_pk, *args, **kwargs):
        user = request.user
        flight = models.Flight.objects.get(pk=flight_pk)
        form = self.form_class(user, flight)
        context = {'form': form}
        return render(request, self.template_path, context)

    def post(self, request, flight_pk, *args, **kwargs):
        user = request.user
        flight = models.Flight.objects.get(pk=flight_pk)
        form = self.form_class(user, flight, request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('aviasales:userflight_reservation_list'))
        context = {'form': form}
        return render(request, self.template_path, context)


class MyFlights(LoginRequiredMixin, View):
    template_path = get_template_path('my_flights')

    def get(self, request):
        user = request.user
        user_flights = models.UserFlight.objects.filter(user__pk=user.pk, approved=True)
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
            user.userflight_set.get(pk=userflight_url_pk, approved=True)
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
            user.userflight_set.get(pk=userflight_url_pk, approved=True)
            return True
        except models.UserFlight.DoesNotExist:
            return False


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


class FlightReviewSelect(View):
    template_path = get_template_path('flight_review_select')

    def get(self, request):
        flights = models.Flight.objects.all()
        return render(request, self.template_path, {'flights': flights})


class FlightReviewList(View):
    template_path = get_template_path('flight_review_list')

    def get(self, request, flight_pk):
        reviews = models.Review.objects.filter(user_flight__flight=flight_pk)
        return render(request, self.template_path, {'reviews': reviews})


@login_required()
def auth_test(request):
    user = request.user
    return HttpResponse(f'Hello {user.get_username()}')
