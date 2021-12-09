from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_email_verified = models.BooleanField(default=True)
    oauth_real_name = models.CharField(max_length=255, blank=True, default='')

    def need_email_verified(self):
        return not self.is_email_verified
