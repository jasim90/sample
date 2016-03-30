from __future__ import unicode_literals

from django.db import models
from django.core import validators
from django.contrib.auth.models import User

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(
        max_length=30,
        validators=[
            validators.RegexValidator(
                regex='^[a-zA-Z0-9]*$',
                message='First name must be Alphabets',
                code='invalid_first_name'
            ),
        ]
    )
    last_name = models.CharField(
        max_length=30,
        validators=[
            validators.RegexValidator(
                regex='^[a-zA-Z0-9]*$',
                message='Last name must be Alphabets',
                code='invalid_last_name'
            )
        ]
    )
    user = models.ForeignKey(User)


class Age(models.Model):
    person = models.ForeignKey(Person)
    age = models.CharField(max_length=3)


class Upload(models.Model):
    file_name = models.CharField(
        max_length=30,
        validators=[
            validators.RegexValidator(
                regex='^[a-zA-Z0-9]*$',
                message='File name must be Alphanumerics',
                code='invalid_file_name'
            ),
        ]
    )
    file = models.FileField()
