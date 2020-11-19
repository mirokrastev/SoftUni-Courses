import os

from django.http import Http404

from pets.models import Like, Pet


class GetPetMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.obj = None

    def dispatch(self, request, *args, **kwargs):
        self.obj = self.get_object()

        if not self.obj:
            raise Http404
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        pet = Pet.objects.get(pk=self.kwargs['pk'])
        if self.request.user.pk != pet.user.pk:
            return False
        return pet


def get_likes(user, pet):
    try:
        return Like.objects.get(user=user, pet=pet)
    except Like.DoesNotExist:
        return None


def delete_image(path):
    if not os.path.exists(path):
        return
    os.remove(path)
