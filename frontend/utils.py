from django.core.exceptions import ObjectDoesNotExist

from methods.models import System_Boundary, Generate_Requirements, User_Sustainability_Indicators, \
    User_Sustainability_Definitions, UserMethods


def hard_reset_data(user):
    """
    Reset data for this user.

    Clearing user data from System_Boundary,
    :param user:
    :return:
    """
    print user
    try:
        objects = System_Boundary.objects.filter(user=user)
    except ObjectDoesNotExist:
        pass
    else:
        for each in objects:
            each.delete()

    try:
        objects = Generate_Requirements.objects.filter(user=user)
    except ObjectDoesNotExist:
        pass
    else:
        for each in objects:
            each.delete()

    try:
        objects = User_Sustainability_Indicators.objects.filter(user=user)
    except ObjectDoesNotExist:
        pass
    else:
        for each in objects:
            each.delete()

    try:
        objects = User_Sustainability_Definitions.objects.filter(user=user)
    except ObjectDoesNotExist:
        pass
    else:
        for each in objects:
            each.delete()

    try:
        objects = UserMethods.objects.filter(user=user)
    except ObjectDoesNotExist:
        pass
    else:
        for each in objects:
            each.delete()

    return True
