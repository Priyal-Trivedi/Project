from django.db import models


class TBL_Scope(models.Model):
    """

    """

    tbl_scope = models.CharField(max_length=255)

    def __unicode__(self):
        """

        :return:
        """
        return self.tbl_scope


class Domain(models.Model):
    """

    """

    domain = models.CharField(max_length=255)

    def __unicode__(self):
        """

        :return:
        """
        return self.domain


class Definitions(models.Model):
    """

    """

    name = models.CharField(max_length=255)
    definition = models.TextField()
    link = models.CharField(max_length=255, null=True)
    tbl_scope = models.ManyToManyField(TBL_Scope, blank=True)
    domain = models.ManyToManyField(Domain, blank=True)
    remarks = models.TextField(null=True)




