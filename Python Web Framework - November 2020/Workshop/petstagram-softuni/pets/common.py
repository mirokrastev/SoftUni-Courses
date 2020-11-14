import os
from pets.models import Like


def get_likes(user, pet):
    try:
        return Like.objects.get(user=user, pet=pet)
    except Like.DoesNotExist:
        return None


def delete_image(path):
    if not os.path.exists(path):
        return
    os.remove(path)
