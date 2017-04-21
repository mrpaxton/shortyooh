
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_url(value):
    url_validator = URLValidator()

    valid_with_prepended = True
    valid_value = True

    try:
        url_validator(value)
    except:
        valid_value = False

    #in case valid URL does not have http in the front
    prepended_value = "http://" + value
    try:
        url_validator(prepended_value)
    except:
        valid_with_prepended = False

    if (not valid_value) and (not valid_with_prepended):
        raise ValidationError("Invalid URL for this filed. \
                from custom validator function")

    return value

def validate_url_with_com(value):
    if not "com" in value:
        raise ValidationError("This is not valid.  No dot com.")
    return value
