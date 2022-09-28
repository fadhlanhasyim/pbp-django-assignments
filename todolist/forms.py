from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(label='title')
    description = forms.CharField(label='description')
    