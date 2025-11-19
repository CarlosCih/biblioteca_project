from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Ejemplo: usuario@ejemplo.com'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Ingrese su contraseña'}),
            'confirm_password': forms.PasswordInput(attrs={'placeholder': 'Confirme su contraseña'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data
    
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Ejemplo: usuario@ejemplo.com'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Ejemplo: Juan'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Ejemplo: Pérez'}),
        }
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(username=self.instance.username).exists():
            raise forms.ValidationError('Este correo electrónico ya está en uso.')
        return email

