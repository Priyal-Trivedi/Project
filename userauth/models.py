from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser, User
from django.db import models
from methods.models import TBL_Scope, Domain
from frontend.forms import PROBLEM_TYPE_CHOICES

class IndeateUserData(User):
    """
    Ignore this class. To be deleted later.
    """

    step= models.IntegerField(default=0)


class UserData(models.Model):
    """

    """

    step_info = models.IntegerField(default=0)
    problem_type = models.CharField(choices=PROBLEM_TYPE_CHOICES, max_length=250, null=True, blank=True)
    domain = models.ForeignKey(Domain, null=True, blank=True)
    tbl_scope = models.ForeignKey(TBL_Scope, null=True, blank=True)



class IndeateUser(User):
    """
    User authorised to login to Indeate and design stuff.
    """

    step_reached = models.IntegerField(default=0, null=True, blank=True)
    # design_data = models.ForeignKey(IndeateUserData, null=True, blank=True)
    design_data = models.ForeignKey(UserData, null=True, blank=True)

    def save_user_progress(self, tbl_scope, domain, problem_type):
        """

        :param tbl_scope:
        :param domain:
        :param problem_type:
        :return:
        """
        tbl_scope = TBL_Scope.objects.get(tbl_scope=tbl_scope)
        domain = Domain.objects.get(domain=domain)
        if self.design_data is None:

            user_data = UserData.objects.create(tbl_scope=tbl_scope,
                                                domain=domain, problem_type=problem_type)
            self.design_data = user_data
            self.save()
        else:
            existing_user_data = self.design_data
            existing_user_data.tbl_scope = tbl_scope
            existing_user_data.domain = domain
            existing_user_data.problem_type = problem_type
            existing_user_data.save()

