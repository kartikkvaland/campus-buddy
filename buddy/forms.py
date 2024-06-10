from .models import *
from django import forms
from django.core.exceptions import ValidationError


class FileSerializers(forms.ModelForm):
    class Meta:
        model = Videos
        fields = ['title', 'description', 'thumbnail', 'video_file']
        
class LoginForm(forms.Form):
    email = forms.EmailField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)
    
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        
        if password != confirm_password:
            raise ValidationError("Passwords do not match")
        return cleaned_data
