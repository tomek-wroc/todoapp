from django import forms
from . import models


class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ['note',  'status', 'location', 'weather', 'temp']

