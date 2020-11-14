from django.contrib.auth.models import User
from accounts.models import UserProfile


def get_user(pk):
    user = User.objects.get(pk=pk)
    return UserProfile.objects.get(user=user)
