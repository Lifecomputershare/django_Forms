from django import forms
from .models import Register

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'
        widget = {
            'name': forms.TextInput(attrs={'class':'hello','placeholder':'Enter your name'}),
            'email': forms.EmailInput(attrs={'class':'email_field','placeholder':'Enter your email'})
        }