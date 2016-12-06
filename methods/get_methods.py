from django.template import Context
from django.template.loader import get_template

from models import System_Boundary, Generate_Requirements, UserMethods


def get_system_boundary(data, user, step):
    """
    Form the HTML context and then send it over as per sustainability definitions.

    :param data:
    :param user:
    :return:
    """
    print data

    html_template = get_template("methods/system_boundary.html")
    if System_Boundary.objects.filter(user=user).count():
        sys_bound = System_Boundary.objects.get(user=user)
        changes_allowed = sys_bound.changes_allowed
        changes_not_allowed = sys_bound.changes_not_allowed

        context = Context({'changes_allowed': changes_allowed, 'changes_not_allowed': changes_not_allowed
                           })
    else:
        context = Context({})

    system_boundary_form_html = html_template.render(context)

    return system_boundary_form_html



def get_generate_requirements(data, user, step):
    """

    :param data:
    :param user:
    :return:
    """

    html_template = get_template("methods/generate_requirements.html")

    if Generate_Requirements.objects.filter(user=user).count():
        gr_obj = Generate_Requirements.objects.get(user=user)
        lc_phase = gr_obj.life_cycle_phases
        issues = gr_obj.issues
        current_systems = gr_obj.current_systems
        requirements = gr_obj.requirements
        print "Sending better context GRQ"
        context = Context({ 'lc_phase': lc_phase, 'issues': issues, 'current_systems': current_systems,
                            'requirements': requirements})
    else:
        context = Context({})


    generate_requirements_html = html_template.render(context)
    return generate_requirements_html


def get_sustainability_definitions(data, user, step):
    """

    :param data:
    :param user:
    :return:
    """

    html_template = get_template("methods/generate_requirements.html")

    if Generate_Requirements.objects.filter(user=user).count():
        gr_obj = Generate_Requirements.objects.get(user=user)
        lc_phase = gr_obj.life_cycle_phases
        issues = gr_obj.issues
        current_systems = gr_obj.current_systems
        requirements = gr_obj.requirements
        print "Sending better context GRQ"
        context = Context({ 'lc_phase': lc_phase, 'issues': issues, 'current_systems': current_systems,
                            'requirements': requirements})
    else:
        context = Context({})


    generate_requirements_html = html_template.render(context)
    return generate_requirements_html


def get_conceptual_design_methods_data(data, user, step):
    """

    :param data:
    :param user:
    :return:
    """
    print "here", data, user, step
    html_template = get_template("methods/methods_display.html")

    if UserMethods.objects.filter(user=user).count():
        user_methods = UserMethods.objects.filter(user=user, step=step)
        indeate_methods = []
        for each in user_methods:
            methods = each.methods.all()
            indeate_methods.extend(methods)

        print indeate_methods

        design_stage = ""
        if step >= 8 and step <= 12:
            design_stage = "Conceptual Design"
        elif step >= 13:
            design_stage = "Embodiment Design"

        context = Context({ 'methods': indeate_methods, 'design_stage': design_stage})
    else:
        print "No details for this user."
        context = Context({})


    generate_requirements_html = html_template.render(context)
    return generate_requirements_html



