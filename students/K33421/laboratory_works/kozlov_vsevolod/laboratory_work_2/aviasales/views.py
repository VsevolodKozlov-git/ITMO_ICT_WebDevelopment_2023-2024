from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView
from django.contrib.auth import get_user_model
from aviasales import models, forms
from aviasales.apps import AviasalesConfig

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


class FlightInfo(View):
    template_path = get_template_path('flight_info')

    def get(self, request, flight_pk):
        user_flights = models.UserFlight.objects.filter(flight__pk=flight_pk)
        context = {'user_flights': user_flights}
        return render(request, self.template_path, context=context)
