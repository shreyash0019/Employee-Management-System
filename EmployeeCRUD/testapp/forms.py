from django import forms
from django.contrib.auth.forms import AuthenticationForm
from testapp.models import Employee

# Employee Form
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

# Custom Login Form (if you want to customize)
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
