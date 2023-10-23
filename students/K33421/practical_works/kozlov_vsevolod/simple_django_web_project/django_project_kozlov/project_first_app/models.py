from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class Car(models.Model):
    serial_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True)

    def get_absolute_url(self):
        return reverse('project_first_app:car_detail', kwargs={'pk': self.pk})




class UserOwner(AbstractUser):
    """
    username
    firstname
    lastname
    """
    birth_date = models.DateField(null=True)
    cars = models.ManyToManyField(Car, through='CarOwn')
    passport_number = models.CharField(max_length=10,
                                       unique=True,
                                       blank=True,
                                       null=True)
    nationality = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=100, blank=True)

    def get_absolute_url(self):
        return reverse('project_first_app:owner_info', args=[str(self.pk)])


class CarOwn(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)


class OwnerLicence(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    Licence_number = models.CharField(max_length=10)
    licence_type = models.CharField(max_length=
                                    10)
    issue_date = models.DateField()