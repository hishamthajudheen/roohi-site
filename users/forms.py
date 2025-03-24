# from django import forms
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from .models import CustomUser

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'phone_number', 'address', 'password1', 'password2']

# class CustomAuthenticationForm(AuthenticationForm):
#     username = forms.CharField(label="Username or Email")

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'address', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-red-400 focus:border-red-400',
                'placeholder': 'Enter your username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-red-400 focus:border-red-400',
                'placeholder': 'Enter your email'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-red-400 focus:border-red-400',
                'placeholder': 'Enter your phone number'
            }),
            'address': forms.Textarea(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-red-400 focus:border-red-400',
                'rows': 3,
                'placeholder': 'Enter your address'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-red-400 focus:border-red-400',
                'placeholder': 'Create a password'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-red-400 focus:border-red-400',
                'placeholder': 'Confirm your password'
            }),
        }
class CustomAuthenticationForm(AuthenticationForm):
        username = forms.CharField(
            label="Username or Email",
            widget=forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-red-400 focus:border-red-400',
                'placeholder': 'Enter your username or email'
            })
        )
        password = forms.CharField(
            widget=forms.PasswordInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-red-400 focus:border-red-400',
                'placeholder': 'Enter your password'
            })
        )
