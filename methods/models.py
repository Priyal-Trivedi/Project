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
    A table in my database: db.sqlite3. Every field is a column.
    Rows - Values in this column.
    """

    name = models.CharField(max_length=255)
    definition = models.TextField()
    link = models.CharField(max_length=255, null=True)
    tbl_scope = models.ManyToManyField(TBL_Scope, blank=True)
    domain = models.ManyToManyField(Domain, blank=True)
    remarks = models.TextField(null=True)


class Indicators(models.Model):
    """

    """

    tbl_scope = models.ForeignKey(TBL_Scope)
    type = models.CharField(max_length=255)
    indicator = models.CharField(max_length=255, null=True)
    tags = models.CharField(max_length=255, null=True, blank=True)


class Procedures(models.Model):
    """

    """

    name = models.CharField(max_length=255)
    steps = models.TextField()


class Methods(models.Model):
    """

    """

    name = models.CharField(max_length=255)
    problem = models.CharField(max_length=255, null=True, blank=True)
    tbl_scope = models.ForeignKey(TBL_Scope, null=True, blank=True)
    stage = models.CharField(max_length=255, null=True, blank=True)
    lcp = models.CharField(max_length=255, null=True, blank=True)
    activity = models.CharField(max_length=255, null=True, blank=True)
    domain = models.CharField(max_length=255, null=True, blank=True)
    time_scale = models.CharField(max_length=255, null=True, blank=True)
    prerequisite = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    input = models.CharField(max_length=255, null=True, blank=True)
    procedure = models.TextField()
    output = models.CharField(max_length=255, null=True, blank=True)
    key_benefits = models.TextField()
    shortcomings = models.CharField(max_length=255, null=True, blank=True)
    example = models.TextField()
    external_link = models.CharField(max_length=255, null=True, blank=True)
    sources = models.CharField(max_length=255, null=True, blank=True)


class System_Boundary(models.Model):
    """

    """

    changes_allowed = models.TextField()
    changes_not_allowed = models.TextField()
    user = models.ForeignKey('userauth.IndeateUser')


class Generate_Requirements(models.Model):
    """

    """

    life_cycle_phases = models.TextField()
    current_systems = models.TextField()
    issues = models.TextField()
    requirements = models.TextField()
    user = models.ForeignKey('userauth.IndeateUser')
