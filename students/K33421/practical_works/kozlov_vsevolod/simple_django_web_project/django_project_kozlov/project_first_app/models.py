from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class Car(models.Model):
    serial_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f'{self.serial_number}'

    def get_absolute_url(self):
        return reverse('project_first_app:car_detail', kwargs={'pk': self.pk})


class UserOwner(AbstractUser):
    birth_date = models.DateField(null=True)
    cars = models.ManyToManyField(Car, through='CarOwn', related_name='userowner_set')
    passport_number = models.CharField(max_length=10,
                                       unique=True,
                                       blank=True,
                                       null=True)
    nationality = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=100, blank=True)


    def get_absolute_url(self):
        return reverse('project_first_app:owner_info', args=[str(self.pk)])


class CarOwn(models.Model):
    owner = models.ForeignKey(get_user_model(), related_name='owner_car', on_delete=models.PROTECT)
    car = models.ForeignKey(Car, on_delete=models.PROTECT, related_name='owner_car')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.owner} {self.car} ' \
               f'{self.start_date.strftime("%Y-%m-%d")} {self.end_date.strftime("%Y-%m-%d")}'


class OwnerLicence(models.Model):
    owner = models.ForeignKey(UserOwner, related_name='owner_licence', on_delete=models.PROTECT)
    licence_number = models.CharField(max_length=10)
    licence_type = models.CharField(max_length=
                                    10)
    issue_date = models.DateField()

    def __str__(self):
        return f'{self.owner} {self.licence_number}'