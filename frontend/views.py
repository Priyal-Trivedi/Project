from django.http import HttpResponseRedirect
from django.shortcuts import render

from forms import DesignChoiceForm

from forms import DOMAIN_CHOICES, PROBLEM_TYPE_CHOICES, TBL_CHOICES
# Create your views here.

def home(request):
    print "Here"
    return render(request, 'index.html')


def data(request):
    return render(request, 'index.html')


def design(request):
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
