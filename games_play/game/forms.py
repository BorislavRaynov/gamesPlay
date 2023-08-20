from django import forms
from .models import Game



class BaseGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

        labels = {
            'max_level': 'Max Level',
            "image": "Image URL",
            "max_level": "Max Level"
        }

class CreateGameForm(BaseGameForm):
    pass


class EditGameForm(BaseGameForm):
    pass


class DeleteGameForm(BaseGameForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'