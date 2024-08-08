from django import forms

class NewIdeaForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField()
