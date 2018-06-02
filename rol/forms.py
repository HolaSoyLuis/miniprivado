from django import forms
from .models import empleado, afiliado, registro

class empleadoForm(forms.ModelForm):
	class Meta:
		model = empleado
		fields = '__all__'

class afiliadoForm(forms.ModelForm):
	class Meta:
		model = afiliado
		fields = '__all__'

class registroForm(forms.ModelForm):
	class Meta:
		model = registro
		fields = '__all__'