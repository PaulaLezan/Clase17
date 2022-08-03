from django import forms #importo la clase forms desde django
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CursoForm (forms.Form):
    nombre = forms.CharField(max_length=50)
    comision= forms.IntegerField()

class ProfeForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()
    profesion= forms.CharField(max_length=50)

class UserRegisterForm (UserCreationForm):
    email = forms.EmailField()
    password1: forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2: forms.CharField(label='Confirmar la contraseña', widget=forms.PasswordInput)

    class Meta:
        model =User 
        fields= ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
