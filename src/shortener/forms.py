
from django import forms
from .validators import validate_url, validate_url_with_com


class SubmitURLForm(forms.Form):
    url = forms.CharField(
        label="Submit URL",
        validators=[validate_url, validate_url_with_com],
    )
