from project_first_app import models
from django.forms import fields_for_model
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


user: models.UserOwner = get_user_model()


class OwnerCreationForm(UserCreationForm):
    class RequiredUserFields:

        def __init__(self):
            self.user_form_fields = fields_for_model(user)

        def get(self, field_name):
            field = self.user_form_fields[field_name]
            field.required = True
            return field

    r = RequiredUserFields()
    email = r.get('email')
    first_name = r.get('first_name')
    last_name = r.get('last_name')
    passport_number = r.get('passport_number')

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'passport_number',
            'birth_date',
            'nationality',
            'address',
            'password1',
            'password2'
        ]

