from django.forms import ModelForm, CheckboxInput

from initiative.models import Character


class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = '__all__'


class CountForm(ModelForm):
    #TODO: if unnique is true render the form as a checkbox
    class Meta:
        Model = Character
        fields = ['name', 'count', 'unique']

    def __init__(self, *args, **kwargs):
        super(CountForm, self).__init__(*args, **kwargs)
        if self.instance.id:
            self.fields['name'].widget.attrs['readonly'] = True


class CharacterCountForm(CountForm):
    def __init__(self, *args, **kwargs):
        super(CharacterCountForm, self).__init__(*args, **kwargs)
        if self.instance.id:
            self.fields['name'].widget.attrs['readonly'] = True
        self.fields['count'].widget = CheckboxInput()

