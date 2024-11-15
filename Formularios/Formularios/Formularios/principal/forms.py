from django import forms
from principal.models import Comuna
class ComunaForm(forms.ModelForm):
    class Meta:
        model = Comuna
        fields = '__all__'