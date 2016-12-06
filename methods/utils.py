from models import Definitions
from models import Indicators

def get_definitions(domain, tbl_scope):
    """
    Based on :problem, :domain and :tbl_scope, fetch all matching definitions.
    :param problem:
    :param domain:
    :param tbl_scope:
    :return:
    """
    definitions = Definitions.objects.filter(tbl_scope__tbl_scope=tbl_scope, domain__domain=domain)
    return definitions


def get_indicators(tbl_scope):
    """
    Based on :tbl_scope, fetch all matching indicators.
    :param problem:
    :param domain:
    :param tbl_scope:K
    :return:
    """
    indicators = Indicators.objects.filter(tbl_scope__tbl_scope=tbl_scope)
    return indicators


def get_indicator_type(tbl_scope):
    """
    Based on :tbl_scope, fetch all matching indicators.
    :param problem:
    :param domain:
    :param tbl_scope:
    :return:
    """
    indicators = Indicators.objects.filter(tbl_scope__tbl_scope=tbl_scope)
    types = [indicator.type for indicator in indicators]

    return set(types)