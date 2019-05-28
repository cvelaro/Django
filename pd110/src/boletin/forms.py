from django import forms

from .models import Registrados

class RegModelForm(forms.ModelForm):
	class Meta:
		model = Registrados
		fields = ["nombre", "email"]

    def clean_email(self):
    	email = self.cleaned_data.get("email")
    	email_base, proveeder = email.split("@")
    	dominio, extension = proveedor.split(".")
    	if not extension == "edu":
    		raise forms.ValidationError("Por favor utiliza un email con la extension .EDU")
    	return email

    def clean_nombre(self):
    nombre = self.cleaned_data.get("nombre")
    #validaciones
    return nombre	

class RegForm(forms.Form):
	nombre = forms.CharField(max_length=50)
	email = forms.EmailField()