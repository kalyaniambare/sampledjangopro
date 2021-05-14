from django import forms
from django.core.exceptions import ValidationError

from core.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'phone_number', 'address']

    def save(self):
        user = super(UserForm, self).save(commit=False)
        user.username = user.email
        user.save()
        return user


class UserFormLogin(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            user = User.objects.filter(email=email, password=password).exists()
            if not user:
                raise ValidationError(
                   "Please check your mail and password"
                )