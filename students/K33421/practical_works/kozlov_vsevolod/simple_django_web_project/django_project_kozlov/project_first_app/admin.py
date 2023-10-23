from django.contrib import admin
from django.contrib.auth import get_user_model
from project_first_app import models


admin.site.register(models.Car)
admin.site.register(get_user_model())
admin.site.register(models.CarOwn)
admin.site.register(models.OwnerLicence)

