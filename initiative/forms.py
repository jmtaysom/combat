from django.forms import ModelForm
from initiative.models import Player, Monster


class CharacterForm(ModelForm):
    class Meta:
        model = Player
        fields = '__all__'


class CountForm(ModelForm):
    class Meta:
        Model = Monster
        fields = ['name', 'count']

    def __init__(self, *args, **kwargs):
        super(CountForm, self).__init__(*args, **kwargs)
        if self.instance.id:
            self.fields['name'].widget.attrs['readonly'] = True


class CharacterCountForm(ModelForm):
    class Meta:
        Model = Player
        fields = ['name', 'present']

    def __init__(self, *args, **kwargs):
        super(CharacterCountForm, self).__init__(*args, **kwargs)
        if self.instance.id:
            self.fields['name'].widget.attrs['readonly'] = True

