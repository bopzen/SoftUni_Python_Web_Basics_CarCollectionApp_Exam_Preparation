# Generated by Django 3.2.19 on 2023-06-22 12:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank='False', max_length=10, null='False', validators=[django.core.validators.MinLengthValidator(2, 'The username must be a minimum of 2 chars')])),
                ('email', models.EmailField(blank='False', max_length=254, null='False')),
                ('age', models.IntegerField(blank='False', null='False', validators=[django.core.validators.MinValueValidator(18)])),
                ('password', models.CharField(blank='False', max_length=30, null='False')),
                ('first_name', models.CharField(blank='True', max_length=30, null='True')),
                ('profile_picture', models.URLField(blank='True', null='True')),
            ],
        ),
    ]