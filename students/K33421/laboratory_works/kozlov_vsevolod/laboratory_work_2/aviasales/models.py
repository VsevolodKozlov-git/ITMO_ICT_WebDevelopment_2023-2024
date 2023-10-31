from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class Flight(models.Model):
    flight_number = models.CharField(max_length=10, blank=False)
    airline = models.CharField(max_length=100, blank=False)
    departure_place = models.CharField(max_length=100, blank=False)
    arrival_place = models.CharField(max_length=100, blank=False)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    gate = models.IntegerField(null=True)

    def clean(self):
        required = [(self.flight_number, 'flight number'),
                    (self.airline, 'airline'),
                    (self.departure_place, 'departure place'),
                    (self.arrival_place, 'arrival place')]

        for field, name in required:
            if not field:
                raise ValidationError(f'{name} is empty')

        if self.departure_time >= self.arrival_time:
            raise ValidationError(f'departure time larger than arrival time')

    def __str__(self):
        return self.flight_number


class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    passport_number = models.CharField(max_length=10, null=True, unique=True, blank=True)
    flights = models.ManyToManyField(Flight, through='UserFlight')

    def __str__(self):
        return f'{self.get_username()}'

    def get_absolute_url(self):
        return reverse('aviasales:user_detail', kwargs={'pk': self.pk})


class UserFlight(models.Model):
    seat_number = models.CharField(max_length=4, blank=False)
    ticket_number = models.CharField(max_length=10, blank=False)
    approved = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

    def clean(self):
        required = [(self.seat_number, 'seat number')]
        for field, name in required:
            if not field:
                raise ValidationError(f'{name} is empty')

    def __str__(self):
        return f'{self.user.get_username()} {self.flight.flight_number}'

    def get_delete_url(self):
        return reverse('aviasales:userflight_delete', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('aviasales:userflight_update', kwargs={'pk': self.pk})


class Review(models.Model):
    user_flight = models.ForeignKey(UserFlight, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    grade = models.IntegerField(validators=[validators.MinValueValidator(0, message='less than 0'),
                                            validators.MaxValueValidator(10, message='larger than 10')])

    def __str__(self):
        return f'{self.user_flight}'
