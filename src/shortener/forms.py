
from django import forms
from .validators import validate_url, validate_url_with_com


class SubmitURLForm(forms.Form):
    url = forms.CharField(
        label="URL(ex: www.duckduckgo.com)",
        validators=[validate_url, validate_url_with_com],
    )
