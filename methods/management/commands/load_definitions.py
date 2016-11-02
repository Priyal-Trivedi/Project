from collections import OrderedDict
from optparse import make_option
from datetime import datetime

from django.core.management import BaseCommand

import pandas as pd
import numpy as np

from methods.models import Domain, TBL_Scope, Definitions


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


def fetch_domains(domains):
    """

    :param domains:
    :return:
    """
    if domains is not np.nan:

        domains = domains.split(",")
        domain_objects = []
        for each in domains:
            each = each.replace(" ", "")
            print each
            try:
                domain_object = Domain.objects.get(domain=each)
            except Exception as e:
                print e
            else:
                if domain_object is not None and domain_object not in domain_objects:
                    domain_objects.append(domain_object)

        return domain_objects
    else:
        return None



class Command(BaseCommand):


    def handle(self, *args, **options):
        """

        :param args:
        :param options:
        :return:
        """

        df = pd.read_csv("definitions.csv")

        for i in range(1,len(df.index)):
            row_dict = df.loc[i].to_dict()

            tbl_scopes = fetch_tbl_scopes(row_dict['tbl_scope'])

            domains = fetch_domains(row_dict['domain'])

            definition = Definitions.objects.create(name=row_dict['name'], definition=row_dict['definition'], link=row_dict['link'],
                                       remarks=row_dict['remarks'])
            if domains is not None:
                definition.domain=domains

            if tbl_scopes is not None:
                definition.tbl_scope = tbl_scopes
            definition.save()