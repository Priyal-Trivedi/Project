from django.template import Context
from django.template.loader import get_template

from utils import get_definitions
from utils import get_indicators, get_indicator_type
from models import System_Boundary, Generate_Requirements
definitions = [
    {'id': 1, 'name': "World Bank", 'definition': """Sustainable development recognizes that growth must be both inclusive and environmentally sound to reduce poverty and build shared prosperity for todays population and to continue to meet the needs of future generations. It is efficient with resources and carefully planned to deliver both immediate and long-term benefits for people   planet   and prosperity.
A sustainable path of development and poverty reduction would be one that (i) manages the resources of our planet for the future generation (ii) ensures social inclusion (iii) adopts fiscally responsible policies that limit future debt burden.""",
     'tbl_scope': 'Environmental,Social,Economic', 'domain': 'Generic', 'remarks': ''},

    {'id': 2, 'name': "State Bank", 'definition': """Sustainable development recognizes that growth must be both inclusive and environmentally sound to reduce poverty and build shared prosperity for todays population and to continue to meet the needs of future generations. It is efficient with resources and carefully planned to deliver both immediate and long-term benefits for people   planet   and prosperity.
    A sustainable path of development and poverty reduction would be one that (i) manages the resources of our planet for the future generation (ii) ensures social inclusion (iii) adopts fiscally responsible policies that limit future debt burden.""",
     'tbl_scope': 'Environmental,Economic', 'domain': 'Manufacturing', 'remarks': ''}
]


def select_system_boundary(data, user):
    """
    Form the HTML context and then send it over as per sustainability definitions.

    :param data:
    :return:
    """


    html_template = get_template("methods/system_boundary.html")
    if System_Boundary.objects.filter(user=user).count():
        sys_bound = System_Boundary.objects.get(user=user)
        changes_allowed = sys_bound.changes_allowed
        changes_not_allowed = sys_bound.changes_not_allowed
        print "Sending better context"
        context = Context({ 'changes_allowed': changes_allowed, 'changes_not_allowed': changes_not_allowed
                           })
    else:
        context = Context({})

    system_boundary_form_html = html_template.render(context)
    return system_boundary_form_html

def generate_requirements(data, user):
    """
    Render HTML context as per generate requirements.
    :param data:
    :return:
    """
    print data
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


def select_sustainability_definitions(data, user):
    """
    Filter sustainability definitions based on tbl_scope and domain.
    :param data:
    :return:
    """

    problem_type = data.get('problem_type')
    domain = data.get('domain')
    tbl_scope = data.get('tbl_scope')

    definitions = get_definitions( domain, tbl_scope)


    html_template = get_template("methods/sustainability_definitions.html")

    names = [each.name for each in definitions]

    context = Context({"names": names})
    sustainability_definitions_html = html_template.render(context)
    return sustainability_definitions_html


    # Form the HTML context and then send it over as per sustainability definitions.
    # return definitions_dict

def select_sustainability_indicators(data, user):
    """

    :param data:
    :return:
    """

    tbl_scope = data.get('tbl_scope')

    types = get_indicator_type(tbl_scope)

    html_template = get_template("methods/sustainability_indicators.html")

    context = Context({"types": types, "tbl_scope": tbl_scope})
    sustainability_indicators_html = html_template.render(context)
    return sustainability_indicators_html



def select_methods_tc_er_mr(data, user):
    """

    :param data:
    :return:
    """
    html_template = get_template("methods/task_clarification/task_clarification_er_mr.html")

    context = Context({})
    select_methods_tc = html_template.render(context)
    return select_methods_tc


def select_methods_tc_s(data, user):
    """

    :param data:
    :return:
    """
    html_template = get_template("methods/task_clarification/task_clarification_s.html")

    context = Context({})
    select_methods_tc = html_template.render(context)
    return select_methods_tc


def conceptual_design_home(data, user):
    """

    :param data:
    :param user:
    :return:
    """

    html_template = get_template("methods/conceptual_design/conceptual_design.html")

    context = Context({})
    conceptual_design_html = html_template.render(context)
    return conceptual_design_html

def conceptual_design_gs(data, user):
    """

    :param data:
    :param user:
    :return:
    """

    html_template = get_template("methods/conceptual_design/conceptual_design_gs.html")

    context = Context({})
    conceptual_design_html = html_template.render(context)
    return conceptual_design_html


def conceptual_design_es_ss(data, user):
    """

    :param data:
    :param user:
    :return:
    """

    html_template = get_template("methods/conceptual_design/conceptual_design_es_ss.html")

    context = Context({})
    conceptual_design_html = html_template.render(context)
    return conceptual_design_html

def conceptual_design_gs_ms(data, user):
    """

    :param data:
    :param user:
    :return:
    """

    html_template = get_template("methods/conceptual_design/conceptual_design_gs_ms.html")

    context = Context({})
    conceptual_design_html = html_template.render(context)
    return conceptual_design_html

def conceptual_design_es_ms(data, user):
    """

    :param data:
    :param user:
    :return:
    """

    html_template = get_template("methods/conceptual_design/conceptual_design_es_ms.html")

    context = Context({})
    conceptual_design_html = html_template.render(context)
    return conceptual_design_html


def embodiment_design_home(data, user):
    """

    :param data:
    :param user:
    :return:
    """

    html_template = get_template("methods/embodiment_design/embodiment_design.html")

    context = Context({})
    conceptual_design_html = html_template.render(context)
    return conceptual_design_html

def embodiment_design_gs(data, user):
    """

    :param data:
    :param user:
    :return:
    """

    html_template = get_template("methods/embodiment_design/embodiment_design_gs.html")

    context = Context({})
    conceptual_design_html = html_template.render(context)
    return conceptual_design_html


def embodiment_design_es_ss(data, user):
    """

    :param data:
    :param user:
    :return:
    """

    html_template = get_template("methods/embodiment_design/embodiment_design_es_ss.html")

    context = Context({})
    conceptual_design_html = html_template.render(context)
    return conceptual_design_html

def embodiment_design_gs_ms(data, user):
    """

    :param data:
    :param user:
    :return:
    """

    html_template = get_template("methods/embodiment_design/embodiment_design_gs_ms.html")

    context = Context({})
    conceptual_design_html = html_template.render(context)
    return conceptual_design_html

def embodiment_design_es_ms(data, user):
    """

    :param data:
    :param user:
    :return:
    """

    html_template = get_template("methods/embodiment_design/embodiment_design_es_ms.html")

    context = Context({})
    conceptual_design_html = html_template.render(context)
    return conceptual_design_html

def detail_design_home(data, user):
    """

    :param data:
    :param user:
    :return:
    """

    html_template = get_template("methods/detail_design/detail_design.html")

    context = Context({})
    conceptual_design_html = html_template.render(context)
    return conceptual_design_html

