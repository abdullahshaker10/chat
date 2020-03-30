from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

GENDER_CHOICES = [
    ('male', 'male'),
    ('female', 'female'),

]


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=200)
    display_name = forms.CharField(max_length=200)
    Gender = forms.CharField(max_length=200, widget=forms.Select(choices=GENDER_CHOICES))

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('name', 'display_name', 'Gender', 'email', 'password1', 'password2')
