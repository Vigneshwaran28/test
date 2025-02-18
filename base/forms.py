from django import forms
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        # exclude = ['user']


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']