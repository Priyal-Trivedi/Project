from collections import OrderedDict
from optparse import make_option
from datetime import datetime

from django.core.management import BaseCommand

import pandas as pd
import numpy as np

from methods.models import Domain, TBL_Scope, Definitions, Indicators


def fetch_tbl_scope(tbl_scope):
    """

    :param tbl_scope:
    :return:
    """

    try:
        # object, created = TBL_Scope.objects.get_or_create(domain=tbl_scope)
        object = TBL_Scope.objects.get(tbl_scope=tbl_scope)
    except Exception as e:
        print e
        return None
    else:
        return object

def fetch_tbl_scopes(tbl_scopes):

    if tbl_scopes is not np.nan:

        tbl_scopes = tbl_scopes.split(",")
        tbl_scope_objects = []
        for each in tbl_scopes:
            each = each.replace(" ", "")
            tbl_scope_object = fetch_tbl_scope(each)
            if tbl_scope_object is not None and tbl_scope_object not in tbl_scope_objects:
                tbl_scope_objects.append(tbl_scope_object)
            else:
                pass
        return tbl_scope_objects
    else:
        return None





class Command(BaseCommand):


    def handle(self, *args, **options):
        """

        :param args:
        :param options:
        :return:
        """

        df = pd.read_csv("indicators.csv")

        for i in range(4, len(df.index)):
            row_dict = df.loc[i].to_dict()

            tbl_scopes = fetch_tbl_scopes(row_dict['TBL_scope'])
            print tbl_scopes

            indicator = Indicators.objects.create(type=row_dict['Type'], indicator=row_dict['Indicators'], tbl_scope=tbl_scopes[0])

            if row_dict['Tags'] is not np.nan:
                indicator.tags = row_dict['Tags']
            else:
                indicator.tags = " "

            indicator.save()