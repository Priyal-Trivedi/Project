import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt

from forms import DesignChoiceForm
from constants import STEPS_NAME, STEPS_METHODS, SAVE_STEPS_METHODS, GET_METHODS_DATA
from forms import DOMAIN_CHOICES, PROBLEM_TYPE_CHOICES, TBL_CHOICES
# Create your views here.
from methods.models import Definitions, Methods, UserMethods
from methods.models import Indicators
from userauth.models import IndeateUser
from django.db.models import Q
def home(request):
    """

    :param request:
    :return:
    """

    if request.user.is_authenticated():
        return render(request, 'instructions.html')
    else:
        return render(request, 'userauth/login.html')


def data(request):
    """

    :param request:
    :return:
    """



    return render(request, 'data.html')

@csrf_exempt
def save_data(request):
    """

    :param request:
    :return:
    """

    if request.POST or request.is_ajax():
        request_parameters = request.POST
        data_save_step = int(request_parameters['step'][0])
        print request.user
        print type(request.user)
        user = IndeateUser.objects.get(username=request.user.username)
        if SAVE_STEPS_METHODS[data_save_step](request_parameters, user):
            return HttpResponse(json.dumps({"success": "True"}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"success": "False"}), content_type="application/json")

    return render(request, 'data.html')\

@csrf_exempt
def save_methods(request):
    """

    :param request:
    :return:
    """

    if request.POST or request.is_ajax():
        request_parameters = request.POST
        methods_list = request_parameters.getlist('methods[]')
        if len(methods_list) > 0:

            user= request.user
            user = IndeateUser.objects.get(username=user.username)
            user_progress = user.step_reached
            user_method = UserMethods.objects.create(user=user, step=user_progress)
            for each_method in methods_list:
                try:
                    method = Methods.objects.get(name=each_method)
                except Exception as e:
                    print e
                    pass
                else:
                    user_method.methods.add(method)
            user_method.save()

            return HttpResponse(json.dumps({"success": "True"}), content_type="application/json")

        else:
            return HttpResponse(json.dumps({"success": "False", "message": "No methods selected to save"}), content_type="application/json")



@csrf_exempt
def fetch_data(request):
    """

    :param request:
    :return:
    """

    if request.POST or request.is_ajax():
        request_parameters = request.POST
        data_save_step = int(request_parameters['step'][0])
        print request.user
        print type(request.user)
        user = IndeateUser.objects.get(username=request.user.username)
        html = GET_METHODS_DATA[data_save_step](request_parameters, user)
        return HttpResponse(json.dumps({"success": "True", 'html': html}), content_type="application/json")

    return render(request, 'data.html')


def design(request):
    """
    Home for the user to choose domain, tbl_scope

    :param request:
    :return:
    """
    #TODO - Based on the step which is saved in indeateuser object's field, take user there.
    print type(request.user)

    user = request.user
    user = IndeateUser.objects.get(username=user.username)
    print user.username
    user_progress = user.step_reached
    print user_progress

    if user_progress > 0:
        context_info_html = next_step(request, user_progress)
        return render(request, 'design_methods.html', {'problem_type': user.design_data.problem_type,
                                                       'tbl_scope': user.design_data.tbl_scope.tbl_scope,
                                                       'domain': user.design_data.domain.domain,
                                                       'rendered_content' : context_info_html,
                                                       'current_step': user.step_reached+1,
                                                       'step_name': STEPS_NAME[str(user.step_reached)]
                                                       })

    else:
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

                # Save the chosen tbl_scope, domain and problem type in user data inforamtion
                user.save_user_progress(tbl_scope, domain, problem_type)

                return render(request, 'design_methods.html', {'problem_type': problem_type,
                                                               'tbl_scope': tbl_scope,
                                                               'domain': domain, 'current_step': 1,
                                                               'initial_content': True})
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
def next_step(request, step_progress=None):
    """

    :param request:
    :return:
    """
    user_obj = IndeateUser.objects.get(username=request.user.username)
    user_data_obj = user_obj.design_data
    if request.POST or request.is_ajax() and (step_progress is None):
        """
        processing POST request or ajax request
        """

        request_parameters = dict(request.POST)

        # This is a front-end request to move ahead to next step.
        current_step = user_obj.step_reached
        next_step = current_step + 1


        tbl_scope = request_parameters.get('tbl_scope')[0]
        domain = request_parameters.get('domain')[0]
        problem_type = request_parameters.get('problem_type')[0]
        step_info = STEPS_NAME[str(next_step)]

        try:
            context_info = STEPS_METHODS[str(next_step)]({'step': next_step, 'tbl_scope': tbl_scope, 'domain': domain,
                                      'problem_type': problem_type}, user_obj)
        except Exception as e:
            print e
            return HttpResponse(json.dumps({"step_info": step_info, 'status': False}),
                                content_type="application/json")
        else:

            # Save the user step progress

            user_obj.step_reached = int(next_step)
            user_obj.save()
            print "current step", next_step
            return HttpResponse(json.dumps({"current_step": next_step+1, 'context_info': context_info, 'step_name': step_info}),
                                content_type="application/json")
    else:
        print step_progress
        try:
            context_info = STEPS_METHODS[str(step_progress)]({'step':step_progress, 'tbl_scope':
                user_data_obj.tbl_scope.tbl_scope, 'domain': user_data_obj.domain.domain,
                                                              'problem_type': user_data_obj.problem_type}, user_obj)
        except Exception as e:
            print e
            return HttpResponse(json.dumps({"step_info": step_progress, 'status': False}),
                                content_type="application/json")
        else:
            print "I'm here and returning "
            return context_info


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

def indicators_list(request):
    """
    Fetch indicators list based on type and tbl_scope
    :param request:
    :return:
    """
    if request.GET or request.is_ajax():
        req_params = dict(request.GET)

        type = req_params['type'][0]
        tbl_scope = req_params['tbl_scope'][0]
        indicator_objects = Indicators.objects.filter(type=type, tbl_scope__tbl_scope=tbl_scope)

        html_template = get_template("methods/indicators_list.html")

        context = Context({"indicators": indicator_objects})
        sustainability_indicators_html = html_template.render(context)

        return HttpResponse(json.dumps({"html": sustainability_indicators_html}), content_type="application/json")


def indicators_info(request):
    """

    :param request:
    :return:
    """
    if request.GET or request.is_ajax():
        req_params = dict(request.GET)

        name = req_params['name'][0]

        indicator_object = Indicators.objects.get(name=name)

        html_template = get_template("methods/indicators_info.html")

        context = Context({"indicator": indicator_object})
        sustainability_indicators_html = html_template.render(context)

        return HttpResponse(json.dumps({"html": sustainability_indicators_html}), content_type="application/json")


def methods_info(request):
    """

    :param request:
    :return:
    """
    print dict(request.GET)
    if request.GET or request.is_ajax():
        req_params = dict(request.GET)
        name = req_params['method'][0]

        method_object = Methods.objects.get(name=name)

        html_template = get_template("methods/methods_info.html")

        context = Context({"method": method_object})
        methods_info_html = html_template.render(context)

        return HttpResponse(json.dumps({"html": methods_info_html}), content_type="application/json")


def fetch_lc_phase(request):
    """

    :param request:
    :return:
    """

    steps_gems_mapping = {8:['Generate', 'Select'], 9:['Evaluate', 'Select'], 10:['Generate', 'Select', 'Modify'],
                          11:['Evaluate', 'Select', 'Modify'], 13:['Generate', 'Select'], 14:['Evaluate', 'Select'],
                          15:['Generate', 'Select', 'Modify'],
                          16:['Evaluate', 'Select', 'Modify'] }

    # Step 12 is starting of 'Embodiment Design'
    if request.GET or request.is_ajax():
        req_params = dict(request.GET)
        print req_params
        user = request.user
        user = IndeateUser.objects.get(username=user.username)
        user_progress = user.step_reached

        print user_progress

        lc_phase = req_params['lc_phase'][0]
        total_methods = []

        # all_methods = Methods.objects.filter(Q(lcp__exact='All'))
        # print all_methods
        #
        # lc_phase_methods = Methods.objects.filter(lcp=lc_phase)
        # print lc_phase_methods
        #


        activity_to_check = steps_gems_mapping[user_progress]
        gems_methods = []
        for each_activity_check in activity_to_check:
            if user_progress > 13:
                methods = Methods.objects.filter(activity__contains=each_activity_check, stage__contains='bodiment', lcp__contains=lc_phase)
            else:
                methods = Methods.objects.filter(activity__contains=each_activity_check, stage__contains='onceptual', lcp__contains=lc_phase)
            print methods
            gems_methods.extend(methods)


        print gems_methods

        for method in gems_methods:
            print method.name

        html_template = get_template("methods/lc_phase.html")

        context = Context({"methods": set(gems_methods)})
        sustainability_indicators_html = html_template.render(context)

        return HttpResponse(json.dumps({"html": sustainability_indicators_html}), content_type="application/json")



def instructions(request):
    print "I'm here in instructions"
    return render(request, 'instructions.html')


def terminology(request):
    """

    :param request:
    :return:
    """

    return render(request, 'terminology.html')


def reset(request):
    """

    :param request:
    :return:
    """
    user =request.user
    try:
        indeate_user = IndeateUser.objects.get(username=user.username)

    except Exception as e:
        print e
        return HttpResponse(json.dumps({"success": 'False'}), content_type="application/json")
    else:
        indeate_user.step_reached=0
        indeate_user.save()
        return HttpResponse(json.dumps({"success": 'True'}), content_type="application/json")




def contribute(request):
    """

    :param request:
    :return:
    """

    return render(request, 'contribute.html')
