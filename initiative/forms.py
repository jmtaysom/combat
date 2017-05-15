from django.forms import ModelForm

from initiative.models import Character


class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = '__all__'