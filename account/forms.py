from django import forms
from .models import Signup, Login


class FormName(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    verify_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Signup
        fields = '__all__'

class LoginName(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = '__all__'
