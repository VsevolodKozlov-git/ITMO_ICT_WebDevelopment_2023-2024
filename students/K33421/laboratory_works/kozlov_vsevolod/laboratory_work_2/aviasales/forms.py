from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import fields_for_model
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