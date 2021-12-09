from django import forms
from django.contrib.auth.password_validation import validate_password
from django.forms import Form, ModelForm
from django.utils.translation import gettext_lazy as _

from dashboard.models import User


class UserNameForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
        ]


class LoginUserResetPasswordForm(Form):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    new_password_re_enter = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(LoginUserResetPasswordForm, self).__init__(*args, **kwargs)

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.user.check_password(old_password):
            raise forms.ValidationError(_("Old password is not correct."))
        return old_password

    def clean_new_password(self):
        new_password = self.cleaned_data.get('new_password')
        validate_password(new_password)
        return new_password

    def clean_new_password_re_enter(self):
        new_password = self.cleaned_data.get('new_password')
        new_password_re_enter = self.cleaned_data.get('new_password_re_enter')
        if new_password != new_password_re_enter:
            raise forms.ValidationError(_("New password and re-enter new password not match."))
        return new_password_re_enter

    def save(self):
        new_password = self.cleaned_data.get('new_password')
        self.user.set_password(new_password)
        self.user.save()
