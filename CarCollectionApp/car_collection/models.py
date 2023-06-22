from django.db import models
from django.core import validators
from CarCollectionApp.car_collection.validators import validate_car_year


class Profile(models.Model):
    MIN_AGE = 18
    MIN_LENGTH_USERNAME = 2
    MAX_LENGTH_USERNAME = 10
    MAX_LENGTH_PASSWORD = 30
    MAX_LENGTH_NAMES = 30

    username = models.CharField(
        max_length=MAX_LENGTH_USERNAME,
        validators=(
            validators.MinLengthValidator(MIN_LENGTH_USERNAME, "The username must be a minimum of 2 chars"),
        ),
        null='False',
        blank='False'
    )
    email = models.EmailField(
        null='False',
        blank='False'
    )
    age = models.IntegerField(
        validators=(
            validators.MinValueValidator(MIN_AGE),
        ),
        null='False',
        blank='False'
    )
    password = models.CharField(
        max_length=MAX_LENGTH_PASSWORD,
        null='False',
        blank='False'
    )
    first_name = models.CharField(
        max_length=MAX_LENGTH_NAMES,
        null='True',
        blank='True'
    )
    last_name = models.CharField(
        max_length=MAX_LENGTH_NAMES,
        null='True',
        blank='True'
    )
    profile_picture = models.URLField(
        null='True',
        blank='True'
    )


class Car(models.Model):
    MAX_TYPE_LENGTH = 10
    MIN_MODEL_LENGTH = 2
    MAX_MODEL_LENGTH = 20
    MIN_PRICE = 1.00

    TYPES = [
        ('Sports Car', 'Sports Car'),
        ('Pickup', 'Pickup'),
        ('Crossover', 'Crossover'),
        ('Minibus', 'Minibus'),
        ('Other', 'Other')
    ]

    type = models.CharField(
        max_length=MAX_TYPE_LENGTH,
        choices=TYPES,
        null='False',
        blank='False'
    )

    model = models.CharField(
        max_length=MAX_MODEL_LENGTH,
        validators=(
            validators.MinLengthValidator(MIN_MODEL_LENGTH),
        ),
        null='False',
        blank='False'
    )

    year = models.IntegerField(
        validators=(
            validate_car_year,
        ),
        null='False',
        blank='False'
    )
    image_url = models.URLField(
        null='False',
        blank='False'
    )
    price = models.FloatField(
        validators=(
            validators.MinValueValidator(MIN_PRICE),
        ),
        null='False',
        blank='False'
    )
