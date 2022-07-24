from django import forms #importo la clase forms desde django

class CursoForm (forms.Form):
    nombre = forms.CharField(max_length=50)
    comision= forms.IntegerField()

class ProfeForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()
    profesion= forms.CharField(max_length=50)