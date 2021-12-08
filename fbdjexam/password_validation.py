import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class CustomPasswordValidator:

    def __init__(self, min_length=1):
        self.min_length = min_length

    def validate(self, password, user=None):
        """
            * contains at least one lower character
            * contains at least one upper character
            * contains at least one digit character
            * contains at least one special character
        """
        if not re.findall(r'[a-z]', password):
            raise ValidationError(
                _('Password must contain at least %(min_length)d lower character.') % {'min_length': self.min_length})
        if not re.findall(r'[A-Z]', password):
            raise ValidationError(
                _('Password must contain at least %(min_length)d upper character.') % {'min_length': self.min_length})
        if not re.findall(r'\d', password):
            raise ValidationError(
                _('Password must contain at least %(min_length)d digit character.') % {'min_length': self.min_length})
        special_characters = re.escape('!@#$%^&*()-_=+{}[]|\\:;<>,.?/')
        if not re.findall(f'[{special_characters}]', password):
            raise ValidationError(
                _('Password must contain at least %(min_length)d special character.') % {'min_length': self.min_length})

    def get_help_text(self):
        return """
            Password should contain at least one lower character.
            Password should contain at least one upper character.
            Password should contain at least one digit character.
            Password should contain at least one special character.
        """
