from django import forms
from django.forms import ModelForm

from .models import*
# creating the same name as the model ending it with form #
class TaskForm(forms.ModelForm):
    title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
    class Meta:
        model = Task
        fields = '__all__'
 