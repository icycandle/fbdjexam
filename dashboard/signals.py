from allauth.account.signals import user_signed_up
from django.dispatch import receiver


@receiver(user_signed_up)
def populate_profile(sociallogin, user, **kwargs):
    email = ''
    first_name = ''
    last_name = ''
    if sociallogin.account.provider == 'facebook':
        user_data = user.socialaccount_set.filter(provider='facebook')[0].extra_data
        email = user_data['email']
        first_name = user_data['first_name']
        last_name = user_data['last_name']

    if sociallogin.account.provider == 'google':
        user_data = user.socialaccount_set.filter(provider='google')[0].extra_data
        email = user_data['email']
        first_name = user_data['given_name']
        last_name = user_data['family_name']

    if email:
        user.email = email
    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name

    user.save(update_fields=['email', 'first_name', 'last_name'])
