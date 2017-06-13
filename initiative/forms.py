import six
from django.forms import ModelForm, CheckboxInput

from initiative.models import Player, Monster

def int_test(v):
    return not (v is 0 or v is None or v == '')

class IntCheckboxInput(CheckboxInput):
    def value_from_datadict(self, data, files, name):
        if name not in data:
            # A missing value means False because HTML form submission does not
            # send results for unselected checkboxes.
            return 0
        value = data.get(name)
        # Translate true and false strings to boolean values.
        values = {'true': True, 'false': False}
        if isinstance(value, six.string_types):
            value = values.get(value.lower(), value)
        return int(bool(value))

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


class CharacterCountForm(CountForm):
    class Meta:
        Model = Player
        fields = ['name', 'present']

    def __init__(self, *args, **kwargs):
        super(CharacterCountForm, self).__init__(*args, **kwargs)
        if self.instance.id:
            self.fields['name'].widget.attrs['readonly'] = True
        self.fields['count'].widget = IntCheckboxInput(check_test=int_test)
