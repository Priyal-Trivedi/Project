from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.

class IndeateUser(User):
    """
    User authorised to login to Indeate and design stuff.
    """

    step_reached = models.IntegerField(default=0)