from django.core import validators


def validate_car_year(value):
    if value < 1980 or value > 2049:
        raise validators.ValidationError("Year must be between 1980 and 2049")