from django.forms import ModelForm

from .models import *

class InputTextForLine(ModelForm):
    class Meta:
        model = TextForLine
        fields = [
            'text',
        ]