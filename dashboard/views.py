from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import TemplateView, FormView

from dashboard.forms import LoginUserResetPasswordForm


class HomeView(TemplateView):
    template_name = 'dashboard/home.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class LoginUserResetPassword(FormView):
    """
    This view is used to reset the password of a user. Has 3 inputs:
    - old_password
    - new_password
    - new_password_confirm
    """
    template_name = 'dashboard/login_user_reset_password.html'
    form_class = LoginUserResetPasswordForm
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

