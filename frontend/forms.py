__author__ = 'priyanktrivedi'
from django import forms
from methods.models import Domain, TBL_Scope

PROBLEM_TYPE_CHOICES = [("product", "Product"), ("manufacturing", "Manufacturing Systems"), ("services", "Services")]

TBL_CHOICES = [(tbl.tbl_scope, tbl.tbl_scope) for tbl in TBL_Scope.objects.all()]

DOMAIN_CHOICES = [(domain.domain, domain.domain) for domain in Domain.objects.all()]


class DesignChoiceForm(forms.Form):
    """
    Form to be rendered for DesignChoices to be made.
    """

    problem_type = forms.ChoiceField(widget=forms.RadioSelect, choices=PROBLEM_TYPE_CHOICES)
    triple_bottom_line = forms.ModelChoiceField(queryset=TBL_Scope.objects.all(), widget=forms.RadioSelect, empty_label=None)
    domain = forms.ModelChoiceField(queryset=Domain.objects.all(), widget=forms.RadioSelect, empty_label=None)
