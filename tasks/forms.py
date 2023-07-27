from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','important']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control','placeholder' : 'Titulo de la Tarea'}),
            'description' : forms.Textarea(attrs={'class':'form-control','placeholder' : 'Descripción de la Tarea'}),
            'important' : forms.CheckboxInput(attrs={'class':'form-check-input text-center'}),
        }