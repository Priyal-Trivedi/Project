from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser, User
from django.db import models


class IndeateUserData(User):
    """
    Ignore this class. To be deleted later.
    """

    step= models.IntegerField(default=0)

class UserData(models.Model):
    """

    """

    step_info = models.IntegerField(default=0)


class IndeateUser(User):
    """
    User authorised to login to Indeate and design stuff.
    """

    step_reached = models.IntegerField(default=0)
    # design_data = models.ForeignKey(IndeateUserData, null=True, blank=True)
    design_data = models.ForeignKey(UserData, null=True, blank=True)