from django import forms
from .models import Recipe
from .mixins import NoLabelSuffixMixin


class RecipeModelForm(NoLabelSuffixMixin, forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('title', 'image_url', 'description', 'ingredients', 'time')

        labels = {
            'time': 'Time (Minutes)',
            'image_url': 'Image URL',
        }
