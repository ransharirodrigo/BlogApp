from django import forms

from .models import CustomUser

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=[
            "first_name",
            "last_name",
            "email",
            "username",
            "password"
        ]