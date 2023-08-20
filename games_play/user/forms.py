from django import forms
from .models import User


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "age", "password"]

        widgets = {
            "password": forms.PasswordInput()
        }


class CreateProfileForm(BaseProfileForm):
    pass


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


