from django import forms

from .models import Registrados

class RegModelForm(forms.ModelForm):
	class Meta:
		model = Registrados
		field = ["nombre", "email"]


class RegForm(forms.Form):
	nombre = forms.CharField(max_length=50)
	email = forms.EmailField()