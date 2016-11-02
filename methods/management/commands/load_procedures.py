from collections import OrderedDict
from optparse import make_option
from datetime import datetime

from django.core.management import BaseCommand

import pandas as pd
import numpy as np

from methods.models import Domain, TBL_Scope, Definitions, Indicators, Procedures


class Command(BaseCommand):


    def handle(self, *args, **options):
        """

        :param args:
        :param options:
        :return:
        """

        df = pd.read_csv("procedures.csv")
        df = df.dropna()
        groups = df.groupby('Design_Methods')

        for name, group in groups:
            values = group.Procedure.values
            steps = ""
            for val in values:
                if steps == "":
                    steps = val
                else:
                    steps = steps + ",\n"+ val

            prod = Procedures.objects.create(name=name, steps=steps)
            prod.save()

