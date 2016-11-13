from models import Definitions


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