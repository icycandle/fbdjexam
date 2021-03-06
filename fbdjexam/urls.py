"""fbdjexam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from dashboard.views import HomeView, LoginUserResetPassword, ResendActivationEmailView, UserNameFormView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('accounts/login-user-reset-password', LoginUserResetPassword.as_view(), name='login_user_reset_password'),
    path('accounts/resend-activation-email', ResendActivationEmailView.as_view(), name='resend_activation_email'),
    path('accounts/user-name-form', UserNameFormView.as_view(), name='user_name_form'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
