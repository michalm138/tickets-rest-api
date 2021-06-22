from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import uuid


def positive_decimal_validator(value):
    if value < 0:
        raise ValidationError("Number value is not positive")


class Country(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return f'{self.name}'


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=45)
    address = models.CharField(max_length=255)
    representative_email = models.EmailField()
    representative_phone = models.CharField(max_length=45, validators=[
        RegexValidator(regex="^(\+?\d*)$", message='Enter a valid value (e.g. +123456789 "+" - optional)')
    ])
    website = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return f'{self.name}'


class Event(models.Model):
    name = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    people_limit = models.PositiveIntegerField(validators=[positive_decimal_validator])
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[positive_decimal_validator])
    age_restrictions = models.PositiveIntegerField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=45)
    address = models.CharField(max_length=255)
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()

    def __str__(self):
        return f'{self.name}'


class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    people = models.PositiveIntegerField(validators=[positive_decimal_validator])
    created_at = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.event}'
