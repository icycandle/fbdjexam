from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_email_verified = models.BooleanField(default=False)
    oauth_real_name = models.CharField(max_length=255, blank=True, default='')

    def need_email_verified(self):
        # ignore oauth user
        if SocialAccount.objects.filter(user=self).exists():
            return False
        email_address = EmailAddress.objects.filter(user=self, primary=True).first()
        if email_address:
            return not email_address.verified
        return False
