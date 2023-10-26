from django.contrib import admin
from aviasales import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Flight)
admin.site.register(models.UserFlight)
admin.site.register(models.Review)
# todo Страница с неподтвержденными билетами