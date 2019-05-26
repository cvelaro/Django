from django import forms

class RegForm(forms.form):
	nombre = forms.CharField(max_length=50)
	edad = forms.InteferField()