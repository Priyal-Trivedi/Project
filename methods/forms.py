

from django import forms
from frontend.forms import DOMAIN_CHOICES


class SystemBoundaryForm(forms.Form):
    """
    Form to be rendered for DesignChoices to be made.
    """

    domain = forms.ChoiceField(widget=forms.RadioSelect, choices=DOMAIN_CHOICES)
