from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import Account


class AccountCreateForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ["email", "first_name", "last_name", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if Account.objects.filter(email=email).exists():
            raise ValidationError(f"O email {email} já está em uso.")
        return email
