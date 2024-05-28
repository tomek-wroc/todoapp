from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['note', 'status', 'location', 'latitude',
                  'longitude', 'weather', 'temp', 'backgroundcolor']
        widgets = {'latitude': forms.HiddenInput(),
                   'longitude': forms.HiddenInput(),
                   'weather': forms.HiddenInput(),
                   'temp': forms.HiddenInput(),
                   'backgroundcolor': forms.HiddenInput(),
                   }
