from models import System_Boundary, Generate_Requirements

def save_system_boundary(data, user):
    """
    Form the HTML context and then send it over as per sustainability definitions.

    :param data:
    :param user:
    :return:
    """
    print data
    changes_allowed = data['changes_allowed']
    changes_not_allowed = data['changes_not_allowed']

    print changes_allowed
    print changes_not_allowed
    try:
        if System_Boundary.objects.filter(user=user).count():

            sys_bound_obj = System_Boundary.objects.get(user=user)
            sys_bound_obj.changes_allowed = changes_allowed
            sys_bound_obj.changes_not_allowed = changes_not_allowed
            sys_bound_obj.save()
            return True
        else:
            sys_bound_obj = System_Boundary.objects.create(changes_allowed=changes_allowed, changes_not_allowed=changes_not_allowed,
                                   user=user)
    except Exception as e:
        print e
        return False
    else:
        return True



def save_generate_requirements(data, user):
    """

    :param data:
    :param user:
    :return:
    """
    print data
    life_cycle_phases = data['lc_phase']
    current_systems = data['current_systems']
    issues = data['issues']
    requirements = data['requirements']
    try:
        if Generate_Requirements.objects.filter(user=user).count():
            generate_req_obj = Generate_Requirements.objects.get(user=user)
            generate_req_obj.life_cycle_phases = life_cycle_phases
            generate_req_obj.current_systems = current_systems
            generate_req_obj.issues = issues
            generate_req_obj.requirements = requirements
            generate_req_obj.save()
            return True
        else:
            generate_req_obj = Generate_Requirements.objects.create(
                life_cycle_phases=life_cycle_phases, current_systems=current_systems, issues=issues,
                requirements=requirements, user=user)
    except Exception as e:
        print e
        return False
    else:
        return True


def save_conceptual_design_gs(data, user):
    """

    :param data:
    :param user:
    :return:
    """
    print data
    return True

def save_conceptual_design_es_ss(data, user):
    """

    :param data:
    :param user:
    :return:
    """
    return True
def save_conceptual_design_gs_ms(data, user):
    """

    :param data:
    :param user:
    :return:
    """

def save_conceptual_design_es_ms(data, user):
    """

    :param data:
    :param user:
    :return:
    """


def save_sustainability_definitions(data, user):
    """

    :param data:
    :param user:
    :return:
    """

    definitions = data.getlist('definitions[]')

    for each in definitions:
        print each
    return True
    # try:
    #     if Generate_Requirements.objects.filter(user=user).count():
    #         generate_req_obj = Generate_Requirements.objects.get(user=user)
    #         generate_req_obj.life_cycle_phases = life_cycle_phases
    #         generate_req_obj.current_systems = current_systems
    #         generate_req_obj.issues = issues
    #         generate_req_obj.requirements = requirements
    #         generate_req_obj.save()
    #         return True
    #     else:
    #         generate_req_obj = Generate_Requirements.objects.create(
    #             life_cycle_phases=life_cycle_phases, current_systems=current_systems, issues=issues,
    #             requirements=requirements, user=user)
    # except Exception as e:
    #     print e
    #     return False
    # else:
    #     return True



def save_sustainability_indicators(data, user):
    """

    :param data:
    :param user:
    :return:
    """

    indicators = data['indicators[]']
    for each in indicators:
        print each
    return True
    # try:
    #     if Generate_Requirements.objects.filter(user=user).count():
    #         generate_req_obj = Generate_Requirements.objects.get(user=user)
    #         generate_req_obj.life_cycle_phases = life_cycle_phases
    #         generate_req_obj.current_systems = current_systems
    #         generate_req_obj.issues = issues
    #         generate_req_obj.requirements = requirements
    #         generate_req_obj.save()
    #         return True
    #     else:
    #         generate_req_obj = Generate_Requirements.objects.create(
    #             life_cycle_phases=life_cycle_phases, current_systems=current_systems, issues=issues,
    #             requirements=requirements, user=user)
    # except Exception as e:
    #     print e
    #     return False
    # else:
    #     return True



