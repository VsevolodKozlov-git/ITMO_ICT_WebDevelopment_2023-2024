from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model
from django.views import View
from project_first_app import forms
from project_first_app import models


class OwnerList(ListView):
    model = get_user_model()

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_staff=False)
        return queryset


class OwnerDetail(DetailView):
    model = get_user_model()

# class OwnerForm(CreateView):
#     model = get_user_model()
#     fields = [
#         'username',
#         'password',
#         'email',
#         'first_name',
#         'last_name',
#         'passport_number',
#         'nationality',
#         'address'
#     ]
#     required_fields = [
#         'first_name',
#         'last_name',
#         'passport_number'
#     ]
#
#     def get_form(self, form_class=None):
#         form = super(OwnerForm, self).get_form(form_class)
#         for field in self.required_fields:
#             form.fields[field].required = True
#         return form


class OwnerForm(View):
    form_class = forms.OwnerCreationForm
    template_name = 'project_first_app/userowner_form.html'


    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = forms.OwnerCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(user.get_absolute_url())
        context = {'form': form}
        return render(request, self.template_name, context)


class CarDetail(DetailView):
    model = models.Car

# def owner_form(request):
#     if request.method == "POST":
#         form = forms.OwnerForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = forms.OwnerForm()
#     return render(request, 'project_first_app/userowner_form.html', {'form': form})
#

class CarCreateView(CreateView):
    model = models.Car
    # template_name = 'project_first_app/car_form.html'
    fields = [
        'serial_number',
        'brand',
        'model'
    ]


class CarUpdateView(UpdateView):
    model = models.Car
    fields = [
        'serial_number',
        'brand',
        'model'
    ]


class CarDeleteView(DeleteView):
    model = models.Car
    success_url = reverse_lazy('project_first_app:owner_list')


