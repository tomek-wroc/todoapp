from django import forms
from django.forms import ModelForm
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['note', 'status', 'location', 'weather', 'temp']
        widgets = {'weather': forms.HiddenInput(),
                   'temp': forms.HiddenInput(),
                   }
