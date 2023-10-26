from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import fields_for_model, ModelForm
from django import forms
from aviasales import models


user = get_user_model()


class UserRegisterForm(UserCreationForm):
    class RequiredUserFields:

        def __init__(self):
            self.user_form_fields = fields_for_model(user)

        def get(self, field_name):
            field = self.user_form_fields[field_name]
            field.required = True
            return field

    r = RequiredUserFields()
    first_name = r.get('first_name')
    last_name = r.get('last_name')
    passport_number = r.get('passport_number')

    class Meta(UserCreationForm.Meta):
        model = user
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'passport_number',
                  'birth_date',
                  'password1',
                  'password2']


class ReviewForm(ModelForm):
    def __init__(self, user_instance, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.update_field_userflights_for_user(user_instance)




    class Meta:
        model = models.Review
        fields = ['user_flight', 'text', 'grade']


    def update_field_userflights_for_user(self, user_instance):
        # default value
        empty_label = ''

        # filter only user's userflights
        # todo  userflight__approved=True
        userflights_set = user_instance.userflight_set.get_queryset()
        if not userflights_set:
            empty_label = 'У вас нет ни одного перелета'
        # remove already reviewed flights
        else:
            revieved_userflights_pk = [i.pk for i in models.Review.objects.all()]
            userflights_set = userflights_set.exclude(pk__in=revieved_userflights_pk)
            if not userflights_set:
                empty_label = 'Вы оценили все перелеты'

        self.fields['user_flight'] = forms.ModelChoiceField(
            queryset=userflights_set,
            empty_label=empty_label)


class ReservationForm(ModelForm):
    def __init__(self, user_instance, flight_instance, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        user_field = self.fields['user']
        user_field.initial = user_instance
        user_field.widget = user_field.hidden_widget()

        flight_field = self.fields['flight']
        flight_field.initial = flight_instance
        flight_field.widget = flight_field.hidden_widget()


    class Meta:
        model = models.UserFlight
        fields = ['seat_number',
                  'user',
                  'flight']