__author__ = 'priyanktrivedi'
from django import forms

PROBLEM_TYPE_CHOICES = [("product", "Product"), ("manufacturing", "Manufacturing Systems"), ("services", "Services")]
TBL_CHOICES = [("environment", "Environment"), ("society", "Society"), ("economy", "Economy")]
DOMAIN_CHOICES = [("environment", "Domain Choice 1"), ("society", "Domain Choice 2"), ("economy", "Domain Choice 3")]


class DesignChoiceForm(forms.Form):
    """
    Form to be rendered for DesignChoices to be made.
    """

    problem_type = forms.ChoiceField(widget=forms.RadioSelect, choices=PROBLEM_TYPE_CHOICES)
    triple_bottom_line = forms.ChoiceField(widget=forms.RadioSelect, choices=TBL_CHOICES)
    domain = forms.ChoiceField(widget=forms.RadioSelect, choices=DOMAIN_CHOICES)
