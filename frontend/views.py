import json

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt

from forms import DesignChoiceForm
from constants import STEPS_NAME, STEPS_METHODS
from forms import DOMAIN_CHOICES, PROBLEM_TYPE_CHOICES, TBL_CHOICES
# Create your views here.
from methods.models import Definitions


def home(request):
    """

    :param request:
    :return:
    """

    if request.user.is_authenticated():
        return render(request, 'index.html')
    else:
        return render(request, 'userauth/login.html')


def data(request):
    return render(request, 'index.html')


def design(request):
    """
    Home for the user to choose domain, tbl_scope

    :param request:
    :return:
    """
    #TODO - Based on the step which is saved in indeateuser object's field, take user there.
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = DesignChoiceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            request_parameters = dict(request.POST)
            problem_type = request_parameters.get('problem_type')[0]
            problem_type = dict(PROBLEM_TYPE_CHOICES).get(problem_type)

            tbl_scope = request_parameters.get('triple_bottom_line')[0]
            tbl_scope = dict(TBL_CHOICES).get(tbl_scope)

            domain = request_parameters.get('domain')[0]
            domain = dict(DOMAIN_CHOICES).get(domain)

            return render(request, 'design_methods.html', {'problem_type': problem_type,
                                                           'tbl_scope': tbl_scope,
                                                           'domain': domain})
        else:
            form = DesignChoiceForm()
    else:
        print "I'm here in get request"
        #TODO : Fetch the step at which the user is currently now and then show the details of that step.

        form = DesignChoiceForm()

    return render(request, 'design.html', {"form": form})


def design_methods(request):
    """

    :param request:
    :return:
    """

    return render(request, 'design_methods.html')
    if request.method == "POST":
        form = DesignChoiceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'design_methods.html')

@csrf_exempt
def next_step(request):
    """

    :param request:
    :return:
    """

    if request.POST or request.is_ajax():
        """
        processing POST request or ajax request
        """
        request_parameters = dict(request.POST)
        print request_parameters
        step = request_parameters.get('step')[0]

        tbl_scope = request_parameters.get('tbl_scope')[0]
        domain = request_parameters.get('domain')[0]
        problem_type = request_parameters.get('problem_type')[0]

        step_info = STEPS_NAME[step]
        context_info = STEPS_METHODS[step]({'step':step, 'tbl_scope': tbl_scope, 'domain': domain,
                                      'problem_type': problem_type})

        return HttpResponse(json.dumps({"step_info": step_info, 'context_info': context_info}), content_type="application/json")


def definitions_info(request):
    """

    :param request:
    :return:
    """
    if request.GET or request.is_ajax():
        req_params = dict(request.GET)
        print "I'm here"
        print req_params
        definition_name = req_params['name'][0]
        definition_object = Definitions.objects.get(name=definition_name)
        print definition_object

        html_template = get_template("methods/definitions_info.html")

        context = Context({"definition": definition_object})
        sustainability_definitions_html = html_template.render(context)

        return HttpResponse(json.dumps({"html": sustainability_definitions_html}), content_type="application/json")


def instructions(request):
    print "I'm here in instructions"
    return render(request, 'instructions.html')


def terminology(request):
    """

    :param request:
    :return:
    """

    return render(request, 'terminology.html')


def contribute(request):
    """

    :param request:
    :return:
    """

    return render(request, 'contribute.html')
