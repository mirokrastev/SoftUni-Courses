from django import template
from accounts.common import get_user
from pets.models import Pet
from pets.views import get_likes

register = template.Library()


@register.inclusion_tag('pets/shared/pet_like_action.html')
def check_for_like(user_pk, pet_pk):
    user = get_user(user_pk)
    pet = Pet.objects.get(pk=pet_pk)
    like = get_likes(user, pet)

    if like:
        return {'can_like': False, 'pet': pet}

    return {'can_like': True, 'pet': pet}
