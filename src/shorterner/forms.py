

from django import forms

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_url(value):
    url_validator = URLValidator()
    try:
        url_validator(value)
    except:
        raise ValidationError("Invalid URL for this filed. from custom validator method")
    return value


def validate_url_with_com(value):
    if not "com" in value:
        raise forms.ValidationError("This is not valid.  No dot com.")
    return value


class SubmitURLForm(forms.Form):
    url = forms.CharField(label="Submit URL", validators=[validate_url, validate_url_with_com])


    """
    #validate form input valid
    #url already in database?

    #call everytime the form_is_valid is called
    #validating on the form
    def clean(self):
        cleaned_data = super(SubmitURLForm, self).clean()
        url = cleaned_data.get('url')
        print("url: ", url)

    #validating on the field, clean_ followed by the field name
    def clean_url(self):
        url = self.cleaned_data.get('url')
        url_validator = URLValidator()
        try:
            url_validator(url)
        except:
            raise forms.ValidationError("Invalid URL for this field")
        return url
    """
